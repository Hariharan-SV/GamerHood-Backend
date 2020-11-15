from flask import Blueprint, request, session
from gamerhood.services.user import getSessionDetails

user = Blueprint('user', __name__, url_prefix="/user")

@user.route('/session/mail',methods=['GET'])
def getMail():
  print(session)
  if('email' in session):
    return session['email']
  else:
    return{"msg":"email not in session"}

@user.route('/session/data',methods=['GET'])
def getSession():
  print(session)
  if('data' in session):
    return session['data']
  elif('email' in session):
    session['data'] = getSessionDetails(session['email'])
    return session['data']
  else:
    return{"msg":"email not in session"}
  

@user.route('/clearSession')
def clearSession():
  try:
    session.clear()
    return {"msg":"Cleared"}
  except:
    return {"msg":"Not Cleared"}

@user.route('/dashboard')
def getDashboard():
  return 'Dashboard'
