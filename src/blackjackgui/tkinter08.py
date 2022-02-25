from tkinterbase import *

class Player:
    seatLocation = {"EAST":(600, 300), "SOUTH":(300, 550), "WEST":(70, 300), "NORTH":(300, 30)}
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
        self.dealBtn = Button(self.root, text="Deal Card", command=self.deal)
        self.dealBtn.place(x=10, y=0)
        self.configBtn = Button(self.root, text="Config", command=self.back)
        self.configBtn.place(x=80, y=0)
        self.updateBtn = Button(self.root, text="Update Results", command=self.update)
        self.updateBtn.place(x=130, y=0)
        self.clearBtn = Button(self.root, text="Clear", command=self.clear)
        self.clearBtn.place(x=220, y=0)
        self.exitBtn = Button(self.root, text="Exit", command=self.exit)
        self.exitBtn.place(x=260, y=0)
        Label(self.root,text="Player Name:").place(x=700, y=0)
        self.nameVar = StringVar()
        self.nameVar.set("East")
        self.playerName = Label(self.root, textvariable=self.nameVar)
        self.playerName.place(x=780, y=0)
        self.hitBtn = Button(self.root, text="Hit", command=self.hit)
        self.hitBtn.place(x=850, y=0)
        self.passBtn = Button(self.root, text="Pass", command=self.pass_)
        self.passBtn.place(x=880, y=0)

        self.buildPlayerList()
        self.displayPlayerNames()

    def deal(self):
        pass

    def back(self):
        pass

    def update(self):
        pass

    def clear(self):
        pass

    def exit(self):
        pass

    def hit(self):
        pass

    def pass_(self):
        pass

    def displayPlayerNames(self):
        for player in self.playerList:
            Label(self.root, text=player.name).place(x=player.getCardX(), y=player.getCardY())

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