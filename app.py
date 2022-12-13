from flask import Flask, redirect, url_for, request, render_template, session
from flask import Flask
from game import Game

app = Flask(__name__)


@app.route("/", methods = ['POST', 'GET'])
def create_game():
    if not request.args or request.args.get("player1") is None or request.args["player1"] == "":
        # TODO: add error flashing
        return render_template("new.html")
    return f"{request.args['player1']} {request.args['player2']}"

