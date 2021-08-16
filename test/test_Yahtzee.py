import unittest
from bad.betterYahtzee import *

class TestCard(unittest.TestCase):
    game = Game()
    john = Player("John")
    david = Player("David")
    game.playerList.append(john)
    game.playerList.append(david)

    def test_roll(self):
        actual = len(self.john.roll())
        self.assertEqual(5, actual)
        actual = len(self.john.roll(3))
        self.assertEqual(3, actual)

    def test_showResult(self):
        self.john.score = 10
        self.david.score = 3
        game.showResult()
