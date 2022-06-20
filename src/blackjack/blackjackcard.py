class Card:
    def __init__(self, face, suit):
        self.face = str(face)
        self.suit = suit
    
    def __repr__(self):
        return f"({self.face}, {self.suit})"

    def __eq__(self, other):
        return self.getValue() == other.getValue()
        
    def __gt__(self, other):
        return self.getValue() > other.getValue()

    def __lt__(self, other):
        return self.getValue() < other.getValue()

    def __add__(self, other):
        return self.getValue() + other.getValue()

    def getValue(self):
        pictured = {"A":1,"J":11,"Q":12,"K":13}
        if self.face.isdigit():
            return int(self.face)
        return pictured.get(self.face, 0)
        
class BlackjackCard(Card):
    def getValue(self):
        switch = {"A":11,"J":10,"Q":10,"K":10}
        if self.face.isdigit():
            return int(self.face)
        return switch.get(self.face)

if __name__ == '__main__':
    heartsQ = BlackjackCard('Q', 'HEARTS') 
    print(heartsQ)
    print(heartsQ.getValue())