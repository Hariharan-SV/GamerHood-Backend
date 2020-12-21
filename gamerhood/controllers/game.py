from flask import Blueprint
from flask.helpers import make_response
from flask.json import jsonify
from gamerhood.helpers.user import token_required
from gamerhood.services.game import get_results_from_keyword

game = Blueprint('game', __name__, url_prefix="/game")

@game.route('/search/<keyword>')
@token_required
def get_matching_games(authorized:bool,keyword:str):
  if not authorized:
    make_response(jsonify({"status": 0, "message": "Token is missing !!"}), 401)
  results = get_results_from_keyword(keyword)
  return make_response(jsonify({"status":1,"data":results[:10]}),200)