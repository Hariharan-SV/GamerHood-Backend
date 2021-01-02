from flask import Blueprint
from datetime import datetime
from flask.helpers import make_response
from flask.json import jsonify
from gamerhood.helpers.user import token_required
from gamerhood.services.game import get_results_from_keyword,get_game_from_id
from gamerhood.services.user import add_game_to_user_searches

game = Blueprint('game', __name__, url_prefix="/game")

@game.route('/search/<keyword>')
@token_required
def get_matching_games(authorized:bool,value:dict,keyword:str):
  if not authorized:
    make_response(jsonify({"status": 0, "message": "Token is missing !!"}), 401)
  results = get_results_from_keyword(keyword)
  return make_response(jsonify({"status":1,"data":results[:10]}),200)

@game.route('/details/<id>')
@token_required
def get_game_details(authorized:bool,value:dict,id:int):
  if not authorized:
    make_response(jsonify({"status": 0, "message": "Token is missing !!"}), 401)
  results = get_game_from_id(id)
  if results is None:
    make_response(jsonify({"status": 0, "message": "No game found!"}), 200)
  return make_response(jsonify({"status":1,"data":results}),200)

@game.route('/add-to-search/<id>')
@token_required
def add_game_to_searches(authorized:bool, value:dict, id:str):
  if not authorized:
    make_response(jsonify({"status": 0, "message": "Token is missing !!"}), 401)
  game_details = get_game_from_id(id)
  if game_details is None:
    make_response(jsonify({"status": 0, "message": "No game found!"}), 200)
  filtered_game_details = {
    "name": game_details["name"], "id": game_details["url_info"]["id"], 
    "imageUrl": game_details["img_url"], "updatedAt": datetime.now().isoformat() }
  result = add_game_to_user_searches(value['userDetails']['email'], filtered_game_details)
  if result == 0:
    make_response(jsonify({"status": 0, "message": "Game not added to history!"}), 200)
  return make_response({"status": 1, "message": "Added game to search history!"}, 200)
