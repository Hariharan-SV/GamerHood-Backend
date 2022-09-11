from pymongo import MongoClient
import os
import re

def get_results_from_keyword(game: str) -> dict:
  client = MongoClient(os.environ.get('database_url'))
  db = client['steam_data']
  collection = db.game_data
  similar_results = collection.find({"url_info.url_name": re.compile(game, re.IGNORECASE)},
   {'_id':0,'url_info.id': 1, 'url_info.type': 1, 'url_info.url_name': 1, 'url_info.url': 1})
  similar_results = [i for i in similar_results]
  return similar_results

def get_game_from_id(game_id: str) -> dict:
  client = MongoClient(os.environ.get('database_url'))
  db = client['steam_data']
  collection = db.game_data
  game = collection.find_one({"url_info.id": game_id})
  if game is not None:
    game.pop("_id",None)
  return game

def checkNotReviewed(user_id: str, game_id: str) -> bool:
  client = MongoClient(os.environ.get('database_url'))
  db = client['steam_data']
  review = db.user_likes.find({"user_id": user_id, "user_data": {
    "$elemMatch": {"game_id": game_id}}})
  return review is None
