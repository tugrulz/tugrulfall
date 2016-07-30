from flask import Flask, render_template, request
from logic import *

app = Flask(__name__)

#PLACES = getPlaces("places.txt");
PLACES = [1,2,3,4,5,6]
games = []
id = 0

@app.route('/', methods=["GET","POST"])
def homepage():
    return render_template("index.html")

def newGame():
    print(request.data)
    if (request.method == "POST"):
        games.append(Game(id+""))
        games[id].addPlayer(request.form.username)
        id = id + 1

def hello_world():
    print("Hello world")
    return 'Hello World!'

# IT WILL REDIRECT TO RANDOM GAME LOBBY
@app.route('/game')
def game():
    return render_template("ingame.html", PLACES = PLACES)

@app.errorhandler(404)
def page_not_found(e):
    return "NOT FOUND"


if __name__ == '__main__':
    app.run()



