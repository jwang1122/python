from tkinterbase import *

class Player:
    seatLocation = {"EAST":(600, 250), "SOUTH":(300, 600), "WEST":(70, 250), "NORTH":(300, 30)}
    def __init__(self, name, seat):
        self.name = name
        self.seat = seat
        self.cardX = Player.seatLocation[seat][0]
        self.cardY = Player.seatLocation[seat][1]

    def __repr__(self) -> str:
        return self.name

    def getCardX(self):
        return self.cardX

    def getCardY(self):
        return self.cardY

class PlayBoard(BaseWindow):
    def buildWidgets(self):
        self.root.title("Blackjack Game")
        Button(self.root, text="Deal Card").pack()
        self.buildPlayerList()
        self.displayPlayerNames()

    def displayPlayerNames(self):
        for player in self.playerList:
            Label(self.root, text=player.name).pack()

    def buildPlayerList(self):
        self.playerList = []
        player = Player("East", "EAST")
        self.playerList.append(player)
        player = Player("South", "SOUTH")
        self.playerList.append(player)
        player = Player("West", "WEST")
        self.playerList.append(player)
        player = Player("Dealer", "NORTH")
        self.playerList.append(player)
        

if __name__ == '__main__':
    PlayBoard()