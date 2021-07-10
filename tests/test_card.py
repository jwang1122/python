import unittest
from src.blackjack.card import Card
"""
1. Suit ignore upper and lower case
2. Could create wrong card
"""
class TestCard(unittest.TestCase):
    def test_faces(self):
        diamondsA = Card("A", "DIAMONDS")
        self.assertEqual(diamondsA.getValue(), 1)
        diamonds8 = Card("8", "DIAMONDS")
        self.assertEqual(diamonds8.getValue(), 8)
        diamonds10 = Card("10", "DIAMONDS")
        self.assertEqual(diamonds10.getValue(), 10)
        diamondsQ = Card("Q", "DIAMONDS")
        self.assertEqual(diamondsQ.getValue(), 12)
        diamondsA = Card("A","Diamonds")
        hearts2 = Card("2", "Hearts")
        self.assertEqual(hearts2>diamondsA, True) # for normal card, A=1 < 2
        heartsJ = Card("J", "Heart")
        self.assertEqual(heartsJ>diamondsQ, False) # for normal card, J=11 < Q=12
        self.assertEqual(heartsJ+diamondsQ, 23)
    
    def test_EqualValue(self):
        diamondsJ = Card("J", "DIAMONDS")
        heartsJ = Card("J", "HEARTS")
        self.assertEquals(diamondsJ.getValue(), heartsJ.getValue())
        self.assertEqual(heartsJ==diamondsJ, True)
        self.assertTrue(diamondsJ==heartsJ)
 