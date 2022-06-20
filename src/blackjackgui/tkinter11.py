from tkinterbase import *
from PIL import ImageTk # Pillow module
import random

class Player:
    seatLocation = {"EAST":(600, 300), "SOUTH":(300, 550), "WEST":(70, 300), "NORTH":(300, 30)}
    def __init__(self, name, seat, screen):
        self.name = name
        self.seat = seat
        self.screen = screen
        self.hand = []
        self.cardX = Player.seatLocation[seat][0]
        self.cardY = Player.seatLocation[seat][1]

    def __repr__(self) -> str:
        return self.name

    def addCardToHand(self, card): # display the card image
        self.hand.append(card)
        cardImage = card.getImage()
        lbl = Label(self.screen)
        lbl.configure(image=cardImage)
        lbl.image = cardImage
        lbl.place(x=self.getCardX(), y=self.getCardY())
        if self.name=="Dealer" and len(self.hand)==2: # disable deal button
            imgFile = 'src/images/backR.gif'
            facedown = ImageTk.PhotoImage(file=imgFile)
            lbl = Label(self.screen)
            lbl.configure(image=facedown)
            lbl.image = facedown
            lbl.place(x=self.getCardX(), y=self.getCardY())
        self.cardX += 30

    def getCardX(self):
        return self.cardX

    def getCardY(self):
        return self.cardY

class Card:
    def __init__(self, face, suit):
        self.face = face
        self.suit = suit
        imgFile = 'src/images/' + self.suit + self.face + '.gif'
        self.image = ImageTk.PhotoImage(file=imgFile)

    def __repr__(self):
        return f"Card({self.face}, {self.suit})"

    def getValue(self):
        imgcard = {"A":11,"J":10,"Q":10,"K":10}
        if self.face in ["A","J","Q","K"]:
            return imgcard[self.face]
        return int(self.face)

    def getImage(self):
        return self.image

class Deck:
    faces = ('A','2','3','4','5','6','7','8','9','10','J','Q','K')
    suits = ('spade','club','diamond','heart')

    def __init__(self):
        self.currentIndex = 52
        self.cards = [Card(face,suit) for face in  self.faces for suit in self.suits]
        self.shuffle()

    def next(self):
        self.currentIndex -= 1
        return self.cards[self.currentIndex]

    def shuffle(self):
        random.shuffle(self.cards)


class Dealer(Player):
    def __init__(self):
        self.name = "Dealer"
        self.seat = "NORTH"
        self.deck = Deck()
        self.hand = []
        self.cardX = Player.seatLocation[self.seat][0]
        self.cardY = Player.seatLocation[self.seat][1]

    def deal(self):
        return self.deck.next()

class PlayBoard(BaseWindow):
    def buildWidgets(self):
        self.dealer = Dealer()
        self.index = 0
        self.root.title("Blackjack Game")
        self.root.configure(bg='#F6D386')
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
        self.setBtnEnabled(self.hitBtn, False)
        self.setBtnEnabled(self.passBtn, False)

        self.buildPlayerList()
        self.displayPlayerNames()

    def deal(self):
        player = self.playerList[self.index]
        player.addCardToHand(self.dealer.deal())
        self.index += 1
        if self.index > 3:
            self.index = 0
        if player.name=="Dealer" and len(player.hand)==2: # disable deal button
            self.dealBtn['state'] = 'disabled'
    
    def setBtnEnabled(self, btn, flag):
        if(flag):
            btn['state'] = 'normal'
        else:
            btn['state'] = 'disabled'

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
            Label(self.root, text=player.name).place(x=player.getCardX()-70, y=player.getCardY())


    def buildPlayerList(self):
        self.playerList = []
        player = Player("East", "EAST", self.root)
        self.playerList.append(player)
        player = Player("South", "SOUTH", self.root)
        self.playerList.append(player)
        player = Player("West", "WEST", self.root)
        self.playerList.append(player)
        player = Player("Dealer", "NORTH", self.root)
        self.playerList.append(player)
        

if __name__ == '__main__':
    PlayBoard()