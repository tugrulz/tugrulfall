import random
import string
def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return "ahmet"
    #return ''.join(random.choice(chars) for _ in range(size))

# Did not make it game-specific to save memory
def getPlaces(filename):
    places = []
    f = open(filename, 'r')
    for line in f:
        #if ((line != "") | (line != "/n")):
        places.append(line[:-1])
    return places

def validityCheck():
    return True

class Player:
    def __init__(self, name):
        self.name = name
        self.type = "CIVILIAN"
        self.voted = False

BASIC_MODE = 0

class Game:
    def __init__(self):
        self.players = {}
        self.playerIDs = []
        self.time = 800
        self.id = id_generator()
        self.place = ""
        self.begun = False
        self.change = False
        self.revealVotes = 0
        self.voteSpyVotes = 0
        self.noEffectRevealVotes = 0
        self.noEffectVoteSpyVotes = 0
        self.agentCount = 0
        self.firstAgent = "no one"
        self.mode = BASIC_MODE

    def __init__(self, name):
        self.players = {}
        self.playerIDs = []
        self.time = 800
        self.id = name
        self.place = ""
        self.begun = False
        self.change = False
        self.revealVotes = 0
        self.voteSpyVotes = 0
        self.agentCount = 0
        self.firstAgent = "no one"
        self.mode = BASIC_MODE

    def setGameID(self, name):
        self.id = name

    def setRandomGameID(self):
        self.id = id_generator()

    def setPlace(self, place):
        self.place = place

    #def addPlayer(self, name, id):


    def addPlayer(self, name):
        self.players[name] = Player(name)
        self.playerIDs.append(name)
        self.change = True

    def assignTypesBasic(self):
        spyID = random.randrange(0, len(self.playerIDs), 1 )
        self.players[self.playerIDs[spyID]].type = "SPY"

    def assignTypes(self):
        if(self.mode != BASIC_MODE):
            spyID = random.randrange(0, len(self.playerIDs), 1 )
            self.players[self.playerIDs[spyID]].type = "SPY"

            agentNum = random.randrange(0, 3, 1)
            self.agentCount = str(agentNum)
            excluded = [spyID]
            for i in range(0, agentNum):
                agentID = random.randrange(0, len(self.playerIDs), 1 )
                while (agentID in excluded):
                    agentID = random.randrange(0, len(self.playerIDs), 1 )
                self.firstAgent = self.playerIDs[agentID]
                excluded.append(agentID)
                self.players[self.playerIDs[agentID]].type = "AGENT NO:00" + (i+1)
        else:
            self.assignTypes()

    def printGameStatus(self):
        if(self.begun):
            print("The game has started.")
        else:
            print("Not started yet.")
        for key in self.players:
            print(self.players[key].name + " is " + self.players[key].type)
        print ("You are in " + self.place)

    # Did not make it game-specific to save memory
    def getPlaces(self, filename):
        places = []
        f = open('workfile', 'r')
        for line in f:
            places.append(line)
        return places

    def start(self):
        print("started")
        self.begun = True
        self.change = True

    def stop(self):
        print("stopped")

    def restart(self):
        print("restarted")

    def voteCheck(self):
        return (len(self.playerIDs) == self.revealVotes + self.voteSpyVotes + self.noEffectVoteSpyVotes + self.noEffectRevealVotes)

    def shouldReveal(self):
        return (self.revealVotes > self.voteSpyVotes) | (self.revealVotes + self.noEffectRevealVotes > self.voteSpyVotes + self.noEffectVoteSpyVotes)






