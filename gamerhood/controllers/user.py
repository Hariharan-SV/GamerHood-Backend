from gamerhood.controllers.auth import get_session
from flask import Blueprint, request, session, jsonify
from flask.helpers import make_response
from gamerhood.helpers.user import token_required

user = Blueprint('user', __name__, url_prefix="/user")

@user.route('/change-password',methods=['POST'])
@token_required
def change_password(authorized:bool):
  if not authorized:
    return make_response({"status": 0, "message": "Token not found !"},401)
  data = request.get_json()
  if(data['password']!=data['retype-password']):
    return make_response({"status": 0, "message": "Passwords Mismatch !"},200)
  user_data = get_session()
  print(user_data)
  return make_response({"status": 1, "message": "Checking !"},200)
