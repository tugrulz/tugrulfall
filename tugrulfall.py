from flask import Flask, render_template, request, url_for, redirect, flash, session, make_response
import os, json
from logic import *

app = Flask(__name__)

import os
cwd = os.getcwd()
os.chdir("./PycharmProjects/tugrulfall")

PLACES = getPlaces("places.txt");
for place in PLACES:
    print(place)
print (PLACES)
#PLACES = ["School", "Public Bus", "Windows"]
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
    error = None
    player = games[gamename].players[request.cookies.get('username')]
    try:
        if (request.method == "POST"):
            actionType = request.form['do']
            print(type(actionType))
            if(actionType == "Reveal Agent"):
                if(player.voted == False):
                    player.voted = True
                    if (player.type == "CIVILIAN"):
                        games[gamename].revealVotes += 1
                    else:
                        games[gamename].noEffectVotes += 1
            elif(actionType == "Vote Spy"):
                if(player.voted == False):
                    player.voted = True
                    if (player.type == "CIVILIAN"):
                        games[gamename].voteSpy += 1
                    else:
                        games[gamename].noEffectVotes += 1
            elif(actionType == "Restart"):
                games[gamename].assignTypesBasic()
                games[gamename].setPlace(PLACES[random.randrange(0, len(PLACES), 1 )])
                games[gamename].start()
                games[gamename].printGameStatus()
                #return redirect(url_for('game', gamename = gamename))
                render_template("ingame.html", PLACES = PLACES, PLAYER = request.cookies.get('username'), GAME = games[gamename] )
            elif(actionType == "Go To New Game"):
                return  render_template("ingame.html", PLACES = PLACES, PLAYER = request.cookies.get('username'), GAME = games[gamename] )

    except Exception as e:
        flash(e)
        return render_template("ingame.html", error = e)
    return render_template("ingame.html", PLACES = PLACES, PLAYER = request.cookies.get('username'), GAME = games[gamename] )

@app.route('/finalDecision/<gamename>')
def finalDecision(gamename):
    if (games[gamename].voteCheck()):
        if (games[gamename].shouldReveal()):
            return games[gamename].firstAgent
        else:
            return "Negative"

@app.route('/lobby/updateLobby/<gamename>')
def update(gamename):
    print (json.dumps(games[gamename].playerIDs))
    return json.dumps(games[gamename].playerIDs)

@app.route('/lobby/startgame/<gamename>')
def start(gamename):
    if(games[gamename].begun):
        print("Game on!!!")
        #return url_for('game', gamename=gamename)
        #return redirect(url_for('game', gamename = gamename))
        return render_template("ingame.html", PLACES = PLACES, GAME = games[gamename])
    else:
        print("Did not begin")
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
    app.run(host= '0.0.0.0')




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