class Card:
    def __init__(self, suit, face):
        self.suit = suit
        self.face = face
    
    def __str__(self):
        return f"{self.suit} of {self.face}"

c11 = Card('CLUB', 'J')
print(c11)
h2 = Card('HEART', 2)
print(h2)