import unittest
from src.blackjack.blackjackcard import BlackjackCard

class TestBlackJackCard(unittest.TestCase):
    def test_faces(self):
        diamondsA = BlackjackCard("A", "DIAMONDS")
        self.assertEqual(diamondsA.getValue(), 11)
        diamonds8 = BlackjackCard("8", "DIAMONDS")
        self.assertEqual(diamonds8.getValue(), 8)
        clubs10 = BlackjackCard("10", "CLUBS")
        self.assertEqual(clubs10.getValue(), 10)
        heartsQ = BlackjackCard("Q", "HEARTS")
        self.assertEqual(heartsQ.getValue(), 10)
        self.assertTrue(clubs10==heartsQ)
