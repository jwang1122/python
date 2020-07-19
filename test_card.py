import unittest
from card import *

class TestBlackJackCard(unittest.TestCase):
    def test_faces(self):
        c1 = BlackJackCard("A", "Diamonds")
        self.assertEqual(c1.getValue(), 11)
        c1 = BlackJackCard("8", "Diamonds")
        self.assertEqual(c1.getValue(), 8)
        c1 = BlackJackCard("10", "Diamonds")
        self.assertEqual(c1.getValue(), 10)
        c1 = BlackJackCard("Q", "Diamonds")
        self.assertEqual(c1.getValue(), 10)
        c1 = Card("A","Diamonds")
        c2 = Card("2", "Hearts")
        self.assertEqual(c2<c1, False)
        c1 = Card("Q","Diamonds")
        c2 = Card("J", "Hearts")
        self.assertEqual(c2<c1, True)
        self.assertEqual(c1+c2, 23)
    
    def test_EqualValue(self):
        c1 = BlackJackCard("J", "Diamonds")
        c2 = BlackJackCard("K", "Hearts")
        self.assertEquals(c1.getValue(), c2.getValue())
        self.assertEquals(c1==c2, True)
 