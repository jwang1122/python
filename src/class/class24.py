from enum import Enum

class Card:
    Face = Enum('Face',("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"))
    Suit = Enum('Suit',('Diamonds', "Clubs", "Spades", "Hearts"))

    def __init__(self, face, suit):
        self.face = face
        self.suit = suit
    
    def __repr__(self):
        return f"({self.face.name}, {self.suit.name})"

    def __eq__(self, other):
        return self.getValue() == other.getValue()

    def __add__(self, other):
        return self.getValue() + other.getValue()

    def getValue(self):
        picture = {'A':1, 'J':11, 'Q':12, 'K':13}
        if self.face.name.isdigit():
            return int(self.face.name)
        return picture.get(self.face.name)


if __name__ == '__main__':
    heartsJ = Card(Card.Face.J, Card.Suit.Hearts)
    print(heartsJ)
    print(heartsJ.getValue())

    diamondsJ = Card(Card.Face.J, Card.Suit.Diamonds)
    print(diamondsJ)
    print(diamondsJ.getValue())

    print(heartsJ==diamondsJ)
    print(heartsJ+diamondsJ)