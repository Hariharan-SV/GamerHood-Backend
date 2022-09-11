from functools import wraps
from flask import request
import jwt, os

def token_required(f):
  @wraps(f)
  def decorator(*args, **kwargs):
    token = None
    authorized = False
    if 'x-auth-token' in request.headers:
      token = request.headers['x-auth-token']
    if token is not None:
      try:
        jwt.decode(token, os.environ.get('key'))
        authorized = True
      except (jwt.ExpiredSignatureError,jwt.InvalidTokenError) as error:
        authorized = False
    return f(authorized,*args, **kwargs)            
  return decorator
