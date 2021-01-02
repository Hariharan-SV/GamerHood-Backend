from functools import wraps
from flask import request
import jwt, os

def token_required(f):
  @wraps(f)
  def decorator(*args, **kwargs):
    token = None
    authorized = False
    value = None
    if 'x-auth-token' in request.headers:
      token = request.headers['x-auth-token']
    if token is not None:
      try:
        value = jwt.decode(token, os.environ.get('key'), algorithms=["HS256"])
        authorized = True
      except jwt.ExpiredSignatureError or jwt.InvalidTokenError:
        authorized = False
    return f(authorized,value,*args, **kwargs)            
  return decorator