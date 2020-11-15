from flask import Blueprint, request, session

game = Blueprint('game', __name__, url_prefix="/game")

@game.route('/session')
def getSession():
  try:
    if(session['email'] is not None):
      return session['email']
    else:
      return 'not defined'
  except KeyError:
    return 'Key error'

@game.route('/')
def getDashboard():
  return 'Game'
