import random

class Player:
    def __init__(self, name):
        self.name = name
        self.type = ""

class Game:
    def __init__(self):
        self.players = []
        self.time = 800
        self.places = []

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

    def setPlaces(self, filename):
        self.places = []

    def stop(self):
        print("stopped")








