from flask import Blueprint, request
from gamerhood.services.auth import validateLogin, validateRegister

auth = Blueprint('auth', __name__, url_prefix="/auth")

@auth.route('/login',methods=['POST'])
def login():
  result = 0
  data = request.get_json()
  try:
    print(data)
    result = validateLogin(data)
  except KeyError:
    return {"status":0,"message":"Keys mismatch"}
  if(result == 1):
    return {"status":1,"message":"Accepted"}
  elif(result == 0):
    return {"status":0,"message":"Passwords mismatch !"}
  else:
    return {"status":0,"message":"Rejected! Username not found"}

@auth.route('/register',methods=['POST'])
def signup():
  data = request.get_json()
  result = 0
  try:
    result = validateRegister(data)
  except KeyError:
    return {"status":0,"message":"Keys mismatch"}
  if(result == 1):
    return {"status":1,"message":"Account Created!"}
  elif(result == -1):
    return {"status":0,"message":"Account creation failed !"}
  else:
    return {"status":0,"message":"Account with mentioned mail-id already exists !"}
