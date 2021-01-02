from pymongo import MongoClient
import os

def add_game_to_user_searches(email:str,record:dict):
  client = MongoClient(os.environ.get('database_url'))
  db = client['steam_data']
  collection = db.users
  try:
    collection.update_one({"email":email},{"$push":{"searches":record}})
  except:
    return 0
  return 1

def get_user_details(email:str):
  val = None
  client = MongoClient(os.environ.get('database_url')) 
  db = client['steam_data'] 
  collection = db.users
  try:
    val = collection.find_one({'email': email})
    val.pop('password',None)
    val.pop('_id',None)
  except:
    return 0, None
  return 1, val
