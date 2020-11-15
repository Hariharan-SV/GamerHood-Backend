from flask import Flask
from flask_cors import CORS

from gamerhood.controllers.auth import auth

app = Flask(__name__)
CORS(app)

# Register API routes
app.register_blueprint(auth)

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
  app.run(debug=True)
