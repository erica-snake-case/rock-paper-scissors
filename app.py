from flask import Flask, redirect, url_for, request, render_template, session
from game import Game
from helpers import get_result

app = Flask(__name__)
app.secret_key =  "STORE_THIS_SECRETLY" # TODO: update to use FLASK-SESSION for server-side storage

# TODO: escape all params

@app.route("/")
def create_game():
    if not request.args or request.args.get("player1") is None or request.args["player1"] == "":
        # TODO: add error flashing
        return render_template("new.html")
    game = Game(request.args["player1"], request.args["player2"]) # TODO: escape
    session["game"] = vars(game)
    return redirect(url_for("play_game"))


@app.route("/game/play")
@app.route("/game/play")
def play_game():
    return render_template("play.html")


@app.route("/game/play/<symbol1>/<symbol2>", defaults={"symbol1": None, "symbol2": None})
@app.route("/game/play/<symbol1>/<symbol2>", methods = ['GET'])
def update_game(symbol1, symbol2):
    result = get_result(symbol1, symbol2)
    # TODO: bug session update isn't working; fix
    session["result"] = result
    session["game"][result] += 1
    return render_template("play.html")

# TODO:
# @app.route("/game/quit")
# save_game() 
# session.pop("game")
#session.pop("results")

# TODO:
# @app.route("/game/load")
# get game from csv dict
# add to session
# redirect to play