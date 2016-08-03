from flask import Flask, render_template, request, url_for, redirect, flash, session, make_response
import os, json
from logic import *

app = Flask(__name__)

#PLACES = getPlaces("places.txt");
PLACES = ["School", "Public Bus", "Windows"]
games = {}

def isIDValid(requestedID):
    return True
    #return games.has_key(requestedID)

@app.route('/', methods=["GET","POST"])
def homepage():
    error = None
    try:
        if (request.method == "POST"):
            actionType = request.form['do']
            print(type(actionType))
            if(actionType == "Join Game"):
                print("1")
                session['username'] = request.form['username']
                #session[request.form['username']] = request.form['username']
                gameID = request.form['gameID']
                print("Joining game with id: " + gameID + " with user named: " + session['username'])
                games[gameID].addPlayer(session['username'])
                resp= make_response(redirect(url_for('lobby', gamename = gameID, playername=request.form['username'])))
                resp.set_cookie('username',request.form['username'])
                return resp
                #return redirect(url_for('lobby', gamename = gameID, playername=request.form['username']))
            else:
                session['username'] = request.form['username']
                #session[request.form['username']] = request.form['username']
                newgame = id_generator()
                games[newgame] = Game(newgame)
                print("Establishing game with id: " + newgame + " with admin named: " + session['username']) #Bad coding, do a hash function here
                games[newgame].addPlayer(session['username'])
                resp= make_response(redirect(url_for('lobby', gamename = newgame, playername=request.form['username'])))
                resp.set_cookie('username',request.form['username'])
                return resp
                #return redirect(url_for('lobby', gamename = newgame, playername=request.form['username']))

    except Exception as e:
        flash(e)
        return render_template("index.html", error = e)
    return render_template("index.html")


# IT WILL REDIRECT TO RANDOM GAME LOBBY
@app.route('/lobby/<gamename>', methods=["GET","POST"])
def lobby(gamename):
    print(gamename)
    error = None
    try:
        if (request.method == "POST"):
            if(validityCheck()):
                print("deneme")
                if(games[gamename].begun == False):
                    games[gamename].assignTypesBasic()
                    games[gamename].setPlace(PLACES[random.randrange(0, len(PLACES), 1 )])
                    games[gamename].start()
                    games[gamename].printGameStatus()
                return redirect(url_for('game', gamename = gamename))
    except Exception as e:
        flash(e)
        return render_template("lobby.html", error = e)

    return render_template("lobby.html", PLAYERS = games[gamename].players)


@app.route('/game/<gamename>')
def game(gamename):
    return render_template("ingame.html", PLACES = PLACES, GAME = games[gamename], PLAYER = request.cookies.get('username'))

@app.route('/lobby/updateLobby/<gamename>')
def update(gamename):
    return json.dumps(games[gamename].playerIDs)

@app.route('/lobby/startgame/<gamename>')
def start(gamename):
    if(games[gamename].begun):
        print("Game on!!!")
        #return url_for('game', gamename=gamename)
        #return redirect(url_for('game', gamename = gamename))
        return render_template("ingame.html", PLACES = PLACES, GAME = games[gamename])
    else:
        print("none")
        return "Negative"




@app.errorhandler(404)
def page_not_found(e):
    return "NOT FOUND"

@app.errorhandler(405)
def method_not_allowed(e):
    flash(e)
    return render_template("index.html", error = e)


if __name__ == '__main__':
    app.secret_key = os.urandom(24)
    app.debug
    app.run()




#@app.route('/joinGame', methods=["GET","POST"])
# def joinGame():
#     error = None
#     try:
#         #print(request.data)
#         #print("1")
#         if (request.method == "POST" & isIDValid(request.form['gameID'])):
#             if(validityCheck()):
#                 print("1")
#                 session['username'] = request.form['username']
#                 gameID = request.form['gameID']
#                 print("Joining game with id: " + gameID + " with user named: " + session['username'])
#                 games[gameID].addPlayer(session['username'])
#                 return redirect(url_for('lobby'), gamename = gameID)
#
#     except Exception as e:
#         flash(e)
#         return render_template("index.html", error = e)
#
#     return render_template("index.html")