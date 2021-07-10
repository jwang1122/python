from enum import Enum


class Suits(Enum):
    SPADE=1
    CLUB=2
    DIAMOND=3
    HEART=4

class Faces(Enum):
    ACE="A"
    TWO="2" 
    THREE="3"
    FOUR="4"
    FIVE="5"
    SIX="6"
    SEVEN="7"
    EIGHT="8"
    NINE="9"
    TEN="10"
    JACK="J"
    QUEEN="Q"
    KING="K"

class Card:
    def __init__(self, face, suit):
        self.face = face
        self.suit = suit

    def __repr__(self):
        return f"({self.face}, {self.suit})"

if __name__ == '__main__':
    for face in Faces:
        print(face)

    for suit in Suits:
        print(suit)
    
    diamondA = Card(Faces.ACE, Suits.DIAMOND)
    print(diamondA)