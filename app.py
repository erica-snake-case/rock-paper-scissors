from flask import Flask, redirect, url_for, request, render_template, session
from game import Game

app = Flask(__name__)


@app.route("/")
def create_game():
    if not request.args or request.args.get("player1") is None or request.args["player1"] == "":
        # TODO: add error flashing
        return render_template("new.html")
    return redirect(url_for("play_game"))


@app.route("/game/play")
@app.route("/game/play")
def play_game():
    return render_template("play.html")
    # return f"{request.args['player1']} {request.args['player2']}"


@app.route("/game/play/<symbol1>/<symbol2>", defaults={"symbol1": None, "symbol2": None})
@app.route("/game/play/<symbol1>/<symbol2>", methods = ['GET'])
def update_game(symbol1, symbol2):
    return render_template("play.html")
    # return f"{request.args['player1']} {request.args['player2']}"

