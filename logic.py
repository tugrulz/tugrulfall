import random

# Did not make it game-specific to save memory
def getPlaces(filename):
    places = []
    f = open(filename, 'r')
    for line in f:
        places.append(line)
    return places

class Player:
    def __init__(self, name):
        self.name = name
        self.type = ""

class Game:
    def __init__(self):
        self.players = []
        self.time = 800
        self.id = ""

    def __init__(self, name):
        self.players = []
        self.time = 800
        self.id = name

    def setGameID(self, name):
        self.id = name

    def addPlayer(self, name):
        self.players.append(Player(name))

    def assignTypes(self):
        spyID = random.randrange(0, len(self.players), 1 )
        self.players[spyID].type = "SPY"

        agentNum = random.randrange(0, 3, 1)
        excluded = [spyID]
        for i in range(0, agentNum):
            agentID = random.randrange(0, len(self.players), 1 )
            while (agentID in excluded):
                agentID = random.randrange(0, len(self.players), 1 )
            excluded.append(agentID)
            self.players[agentID].type = "AGENT NO:00" + (i+1)

    # Did not make it game-specific to save memory
    def getPlaces(self, filename):
        places = []
        f = open('workfile', 'r')
        for line in f:
            places.append(line)
        return places

    def stop(self):
        print("stopped")








