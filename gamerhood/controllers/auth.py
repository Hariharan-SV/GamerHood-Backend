from flask import Blueprint, request, session
from gamerhood.services.auth import validateLogin, validateRegister

auth = Blueprint('auth', __name__, url_prefix="/auth")

@auth.route('/session')
def getSession():
  try:
    if(session['email'] is not None):
      return session['email']
    else:
      return 'not defined'
  except KeyError:
    return 'Key error'

@auth.route('/login',methods=['POST'])
def login():
  result = 0
  data = request.get_json()
  try:
    result = validateLogin(data)
  except KeyError:
    return {"status":0,"message":"Keys mismatch"},400
  if(result == 1):
    session['email'] = data['email']
    print(session)
    return {"status":1,"message":"Accepted"},200
  elif(result == 0):
    return {"status":0,"message":"Passwords mismatch !"},200
  else:
    return {"status":0,"message":"Rejected! Username not found"},200

@auth.route('/register',methods=['POST'])
def signup():
  data = request.get_json()
  result = 0
  try:
    result = validateRegister(data)
  except KeyError:
    return {"status":0,"message":"Keys mismatch"}
  if(result == 1):
    session['email'] = data['email']
    return {"status":1,"message":"Account Created!"},200
  elif(result == -1):
    return {"status":0,"message":"Account creation failed !"},400
  else:
    return {"status":0,"message":"Account with mentioned mail-id already exists !"},200
