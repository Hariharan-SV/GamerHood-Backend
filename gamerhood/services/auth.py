# importing module 
from pymongo import MongoClient

def validateLogin(record:dict)->int:
  # Connect with the portnumber and host 
  client = MongoClient("mongodb+srv://deepan:deepan2000@cluster0.52jwx.mongodb.net/steam_data?retryWrites=true&w=majority") 
  # Access database 
  db = client['steam_data'] 
  collection = db.users
  # Access collection of the database 
  print(record)
  try:
    val = collection.find_one({'email': record['email']})
    if(val['password'] != record['password']):
      return 0
  except:
    return -1
  # return 1 for successful login
  return 1

def validateRegister(record:dict)->int:
  # Connect with the portnumber and host 
  client = MongoClient("mongodb+srv://deepan:deepan2000@cluster0.52jwx.mongodb.net/steam_data?retryWrites=true&w=majority") 
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
