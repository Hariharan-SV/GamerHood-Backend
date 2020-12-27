from flask import Flask
from flask_cors import CORS

from gamerhood.controllers.auth import auth
from gamerhood.controllers.user import user
from gamerhood.controllers.game import game

app = Flask(__name__)

# Register API routes
app.register_blueprint(auth)
app.register_blueprint(user)
app.register_blueprint(game)

@app.errorhandler(404)
def handle_404(e):
  return "There is nothing here", 404

@app.errorhandler(405)
def handle_405(e):
  return "Wrong request method", 405

@app.route('/')
def hello_world():
  return 'Hello World!'

if __name__ == '__main__':
  app.secret_key = 'super secret key'
  app.config['SESSION_TYPE'] = 'filesystem'
  app.config['CORS_HEADERS'] = 'Content-Type'
  app.run(debug=True,port=5500)