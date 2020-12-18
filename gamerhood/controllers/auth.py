from flask import Blueprint, request, jsonify
from flask.helpers import make_response
from gamerhood.services.auth import validateLogin, validateRegister
import jwt
from datetime import datetime,timedelta
import os

auth = Blueprint('auth', __name__, url_prefix="/auth")

@auth.route('/session')
def getSession():
	token = None
	data = {"status": 0, "message": "Pending"}
	if 'x-auth-token' in request.headers:
		token = request.headers['x-auth-token']
	if token is None:
		return make_response(jsonify({"status": 0, "message": "Token is missing !!"}), 401)
	try:
		data = jwt.decode(token, os.environ.get('key'))
		data["status"] = 1
	except:  # TODO : GET Type of error name when unable to decode
		return make_response(jsonify({"status": 0, "message": "Token is invalid !!"}), 401)
	return make_response(jsonify(data), 200)


@auth.route('/login', methods=['POST'])
def login():
	result = 0
	data = request.get_json()
	try:
		result, value = validateLogin(data) # TODO : Convert to snake_case
	except KeyError:
		return make_response({"status": 0, "message": "Keys mismatch"}, 400)
	if result == 1:
		print(value)
		token = jwt.encode({
			'userDetails': value,
			'exp': datetime.now() + timedelta(days=3)
		}, os.environ.get('key'))
		return make_response({"status": 1, "message": "Accepted", "token": token.decode('utf-8')}, 200)
	elif(result == 0):
		return make_response({"status": 0, "message": "Passwords mismatch !"}, 200)
	else:
		return make_response({"status": 0, "message": "Rejected! Username not found"}, 404)


@auth.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	result = 0
	try:
		result = validateRegister(data) # TODO : Convert to snake_case
	except KeyError:
		return make_response({"status": 0, "message": "Keys mismatch"}, 200)
	if result == 1: # TODO: Remove unnecessary condition brackets
		data.pop('password', None)
		token = jwt.encode({
			'userDetails': data,
			'exp': datetime.now() + timedelta(days=3) # TODO Fix datetime import
		}, os.environ.get('key'))
		return make_response({"status": 1, "message": "Account Created!", "token": token}, 200)
	elif(result == -1):
		return make_response({"status": 0, "message": "Account creation failed !"}, 400)
	else:
		return make_response({"status": 0, "message": "Account with mentioned mail-id already exists !"}, 200)
