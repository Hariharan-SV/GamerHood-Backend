# importing module 
from pymongo import MongoClient
import os

def validateLogin(record:dict)->int:
  # Connect with the portnumber and host 
  client = MongoClient(os.environ.get('database_url')) 
  # Access database 
  db = client['steam_data'] 
  collection = db.users
  # Access collection of the database 
  print(record)
  try:
    val = collection.find_one({'email': record['email']})
    if(val['password'] != record['password']):
      return 0, None
  except:
    return -1, None
  # return 1 for successful login
  val.pop('password',None)
  val.pop('_id',None)
  return 1,val

def validateRegister(record:dict)->int:
  # Connect with the portnumber and host 
  client = MongoClient(os.environ.get('database_url')) 
  # Access database 
  db = client['steam_data'] 
  try:
    # Access collection of the database 
    count = db.users.count({'email': record['email']})
    if(count != 0):
      return 0
    else:
      res = db.users.insert(record)
  except:
    return -1
  # return 1 for successful register
  return 1
