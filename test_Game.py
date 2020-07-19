import unittest
from card import *

class TestPlayer(unittest.TestCase):
    def test_determineWiner(self):
        game = Game()
        john = Player("John")
        ailian = Player("Ailian")
        game.addPlayer(john)
        game.addPlayer(ailian)

        hj = BlackJackCard("J", "Hearts")
        c3= BlackJackCard("3", "Clubs")
        cq= BlackJackCard("Q", "Clubs")
        ailian.addCardToHand(hj)
        ailian.addCardToHand(c3)
        ailian.addCardToHand(cq)

        s5 = BlackJackCard("5", "Spades")
        h9= BlackJackCard("9", "Hearts")
        h10= BlackJackCard("10", "Hearts")
        john.addCardToHand(s5)
        john.addCardToHand(h9)
        john.addCardToHand(h10)

        c6 = BlackJackCard("6", "Clubs")
        d3 = BlackJackCard("3", "Diamonds")
        d6= BlackJackCard("6", "Diamonds")
        dq= BlackJackCard("Q", "Diamonds")
        game.dealer.addCardToHand(c6)
        game.dealer.addCardToHand(d3)
        game.dealer.addCardToHand(d6)
        game.dealer.addCardToHand(dq)
        
        game.determineWiner()
        self.assertEqual(ailian.win, 0)
        self.assertEqual(john.win, 0)
        self.assertEqual(game.dealer.win, 0)
