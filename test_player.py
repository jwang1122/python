import unittest
from card import *

class TestPlayer(unittest.TestCase):
    def test_getHandValue277(self):
        john = Player("John")
        d2 = BlackJackCard("2", "Diamonds")
        h7= BlackJackCard("7", "Hearts")
        c7= BlackJackCard("7", "Clubs")
        
        john.addCardToHand(d2)
        john.addCardToHand(h7)
        john.addCardToHand(c7)
        self.assertEqual(john.getHandValue(), 16)

    def test_getHandValue4Q8(self):
        john = Player("John")
        d2 = BlackJackCard("4", "Diamonds")
        h7= BlackJackCard("Q", "Hearts")
        c7= BlackJackCard("8", "Clubs")
        
        john.addCardToHand(d2)
        john.addCardToHand(h7)
        john.addCardToHand(c7)
        self.assertEqual(john.getHandValue(), 22)
        
    def test_getHandValueA77(self):
        john = Player("John")
        dA = BlackJackCard("A", "Diamonds")
        h7= BlackJackCard("7", "Hearts")
        c7= BlackJackCard("7", "Clubs")
        
        john.addCardToHand(dA)
        john.addCardToHand(h7)
        john.addCardToHand(c7)
        self.assertEqual(john.getHandValue(), 15)
    
    def test_hit(self):
        john = Player("John")
        dA = BlackJackCard("2", "Diamonds")
        h7= BlackJackCard("5", "Hearts")
        c7= BlackJackCard("3", "Clubs")
        john.addCardToHand(dA)
        john.addCardToHand(h7)
        john.addCardToHand(c7)
        self.assertEqual(john.hit(), True)

        c4 = BlackJackCard("A","Hearts")
        john.addCardToHand(c4)
        self.assertEqual(john.hit(), False)

    def test_clean(self):
        john = Player("John")
        dA = BlackJackCard("2", "Diamonds")
        h7= BlackJackCard("5", "Hearts")
        c7= BlackJackCard("3", "Clubs")
        john.addCardToHand(dA)
        john.addCardToHand(h7)
        john.addCardToHand(c7)
        john.cleanHand()
        self.assertEqual(len(john.hand), 0)        
