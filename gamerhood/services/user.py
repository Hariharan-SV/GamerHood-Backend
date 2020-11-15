# importing module 
from pymongo import MongoClient

def getSessionDetails(email:str)->dict:
  # Connect with the portnumber and host 
  client = MongoClient("mongodb+srv://deepan:deepan2000@cluster0.52jwx.mongodb.net/steam_data?retryWrites=true&w=majority") 
  # Access database 
  db = client['steam_data'] 
  collection = db.users
  # Access collection of the database 
  try:
    val = collection.find_one({'email': email},{'_id':0})
    print("Found one",val)
  except:
    print('Exception !')
    return {'msg':'not found'}
  # return 1 for successful login
  return val