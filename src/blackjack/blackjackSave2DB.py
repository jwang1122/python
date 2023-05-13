import random
from blackjackdb import BlackJackDB
import uuid

class Card:
    def __init__(self, face, suit):
        self.face = face
        self.suit = suit
        
    def __repr__(self):
        return f'({self.face}, {self.suit})'

    def getValue(self):
        # Implementation of the method to get the numerical value of the card
        if self.face == 'A':
            return 1
        if self.face == 'J':
            return 11
        if self.face == 'Q':
            return 12
        if self.face == 'K':
            return 13

        return int(self.face)

    def getValue(self): # this is a better version of the getValue() function
        if self.face.isdigit():
            return int(self.face)
        pictured = {'A':1, 'J':11, 'Q':12, 'K':13}
        return pictured[self.face]


class BlackjackCard(Card):
    def getValue(self): # this function override the same function defined in its superclass
        if self.face.isdigit():
            return int(self.face)
        pictured = {'A':11, 'J':10, 'Q':10, 'K':10}
        return pictured[self.face]

    def getValue(self): # this function override the same function defined in its superclass
        if self.face in ['J','Q','K']:
            return 10
        if self.face == 'A':
            return 11
        return int(self.face)

class Deck:
    FACES = ('A','2','3','4','5','6','7','8','9','10','J','Q','K') # class level attribute
    SUITS = ('SPADES','CLUBS','DIAMONDS','HEARTS')
    def __init__(self):
        self.topCardIndex = 0
        self.stackOfCards = [BlackjackCard(face, suit) for face in Deck.FACES for suit in Deck.SUITS]
        # ChatGPT generated code below
        # self.topCardIndex = 0
        # self.stackOfCards = []
        # for suit in ['Hearts', 'Diamonds', 'Clubs', 'Spades']:
        #     for face in range(2, 11):
        #         self.stackOfCards.append(Card(str(face), suit))
        #     for face in ['J', 'Q', 'K', 'A']:
        #         self.stackOfCards.append(BlackjackCard(face, suit))

    def __len__(self):
        return len(self.stackOfCards)

    def __repr__(self):
        return str(self.stackOfCards) # use str() built in function to convert a list to a string

    def shuffle(self):
        random.shuffle(self.stackOfCards)

    def nextCard(self):
        card = self.stackOfCards[self.topCardIndex]
        self.topCardIndex += 1
        return card

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.winCount =0

    def __repr__(self):
        return self.name
    
    def win(self):
        self.winCount += 1

    def addCardToHand(self, card):
        self.hand.append(card)

    def getHandSize(self):
        return len(self.hand)

    def getHandValue(self):
        value = 0
        aceCount = 0
        for card in self.hand:
            if card.face == 'A':
                aceCount += 1
            value += card.getValue()
        while aceCount > 0:
            if value > 21:
                value -= 10  # this will make original A=11 to A=1
            aceCount -= 1
        return value


    def showHand(self):
        print(f'{self.name}: {self.hand}-{self.getHandValue()}')

    def hit(self):
        answer = input(f"{self.name}: hit? (y/n) ")
        return answer =='y'
    

class Dealer(Player):
    def __init__(self):
        self.name = "Dealer"
        self.hand = []
        self.winCount = 0
        self.deck = Deck()
    
    def shuffle(self):
        self.deck.shuffle()

    def deal(self):
        return self.deck.nextCard()

    def showHand(self, shown):
        if len(self.hand) == 2 and not shown:
            print(f'{self.name}: [{self.hand[0]}, HIDDEN]')
        else:
            super().showHand()

    def hit(self):
        value = super().getHandValue()
        if value < 17:
            return True
        return False

class Game:
    def __init__(self):
        self.playerList = []
        self.dealer = Dealer()
        self.buildPlayerList()
        self.db = BlackJackDB('data/blackjack.db')

    def buildPlayerList(self):
        more = True
        while(more):
            name = input("Please enter player name: ")
            player = Player(name)
            self.playerList.append(player)
            answer = input("more player?(y/n) ")
            if answer == 'n':
                more = False

    def dealCard(self):
        for player in self.playerList:
            player.addCardToHand(self.dealer.deal())
        self.dealer.addCardToHand(self.dealer.deal())
    
    def showHand(self):
        for player in self.playerList:
            player.showHand()
        self.dealer.showHand(False)

    def dealCards(self):
        self.dealCard()
        self.showHand()  # duplicate this line==> Shift+Alt > Down Arrow
        self.dealCard()  # move the line ==> Alt > Downarrow
        self.showHand()

    def clearHand(self):
        for player in self.playerList:
            player.clearHand()
        self.dealer.clearHand()

    def play(self):
        print("Game start...")
        self.dealer.shuffle()
        while(True):
            self.dealCards()
            for player in self.playerList:
                while player.hit():
                    player.addCardToHand(self.dealer.deal())
                    player.showHand()
            while self.dealer.hit():
                self.dealer.addCardToHand(self.dealer.deal())
            self.dealer.showHand(True)
            self.determineWinner()
            answer = input("Another round? (y/n) ")
            if answer == 'n':
                break
            self.clearHand()    
        print("Game over!")

    def store(self, name, /, *, win=0, loss=0, tie=0):
        blackjack = {
            "id":uuid.uuid4().hex,
            'name':name,
            'win':win,
            "loss":loss,
            "tie":tie,
        }
        self.db.create(blackjack)

    def determineWinner(self):
        dealerTotal = self.dealer.getHandValue()
        for player in self.playerList:
            playerTotal = player.getHandValue()
            if playerTotal > 21:
                self.store(player.name, loss=1)
                self.store(self.dealer.name, win=1)
                self.dealer.win()
            elif dealerTotal > 21:
                self.store(player.name, win=1)
                self.store(self.dealer.name, loss=1)
                player.win()
            elif dealerTotal == playerTotal:
                self.store(player.name, tie=1)
                self.store(self.dealer.name, tie=1)
            elif playerTotal > dealerTotal:
                self.store(player.name, win=1)
                self.store(self.dealer.name, loss=1)
                player.win()
            else:
                self.store(player.name, loss=1)
                self.store(self.dealer.name, win=1)
                self.dealer.win()
            print(f'{player.name}: {player.winCount}')
        print(f'{self.dealer.name}: {self.dealer.winCount}')

if __name__ == '__main__':
    # test Game
    blackjack = Game()
    # print(blackjack.playerList)
    blackjack.play()
    # print(blackjack.dealer.getHandSize())
    # print(blackjack.dealer.hand)


    # test code for Player
    # john = Player("John")
    # print(john)
    # john.addCardToHand(BlackjackCard("2","HEARTS"))
    # john.addCardToHand(BlackjackCard("Q","HEARTS"))
    # john.addCardToHand(BlackjackCard("10","HEARTS"))
    # print(john.getHandSize())
    # john.showHand()
    # print(john.getHandValue())

    # dealer = Dealer()
    # print(dealer)
    # dealer.addCardToHand(BlackjackCard("A","CLUBS"))
    # print(dealer.getHandSize())
    # dealer.showHand()
    # print(dealer.getHandValue())
    # dealer.shuffle()
    # card = dealer.deal()
    # print(card)
    # card = dealer.deal()
    # print(card)

    # test code for Deck class
    # deck = Deck()
    # print(deck)
    # print(len(deck))
    # deck.shuffle()
    # print(deck)
    # print(len(deck))
    # card = deck.nextCard()
    # print(card)
    # card = deck.nextCard()
    # print(card)
    # card = deck.nextCard()
    # print(card)

    # test code for Card 
    # club2 = Card('2', 'club')
    # print(club2, club2.getValue(), sep='::') # sep is a keyword argument
    # heartQ = Card('Q', 'heart')
    # print(heartQ, heartQ.getValue())
    # spade10 = Card('10', 'spade')
    # print(spade10, spade10.getValue())
    # diamondA = Card('A', 'diamond')
    # print(diamondA, diamondA.getValue())

    # test code for BlackjackCard
    # club2 = BlackjackCard('2', 'club')
    # print(club2, club2.getValue(), sep='::') # sep is a keyword argument
    # heartQ = BlackjackCard('Q', 'heart')
    # print(heartQ, heartQ.getValue())
    # spade10 = BlackjackCard('10', 'spade')
    # print(spade10, spade10.getValue())
    # diamondA = BlackjackCard('A', 'diamond')
    # print(diamondA, diamondA.getValue())
