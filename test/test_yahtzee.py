import unittest
from src.yahtzee.score import *

class TestScore(unittest.TestCase):

    def test_upperSection(self):
        d = [1,2,3,4,5]
        actual = upperSection(d)
        self.assertEqual(15, actual)
        d = [3,3,3,4,4]
        actual = upperSection(d)
        self.assertEqual(17, actual)

    def test_kind(self):
        d = [2,2,2,3,5]
        actual = kind(d)
        self.assertEqual(3, actual)
        d = [2,2,2,2,5]
        actual = kind(d)
        self.assertEqual(4, actual)

    def test_fullHouse(self):
        d = [2,2,2,3,3]
        actual = fullHouse(d)
        self.assertTrue(actual)

        d = [2,2,2,3,5]
        actual = fullHouse(d)
        self.assertFalse(actual)

    def test_smallStraight(self):
        d = [1,2,3,4,4]
        actual = smallStraight(d)
        self.assertTrue(actual)
        d = [1,2,3,4,5]
        actual = smallStraight(d)
        self.assertFalse(actual)

    def test_largeStraight(self):
        d = [1,2,3,4,5]
        actual = largeStraight(d)
        self.assertTrue(actual)

        d = [1,2,3,4,4]
        actual = largeStraight(d)
        self.assertFalse(actual)

    def test_yahtzee(self):
        d = [2,2,2,2,2]
        actual = yahtzee(d)
        self.assertTrue(actual)

        d = [2,2,2,2,1]
        actual = yahtzee(d)
        self.assertFalse(actual)

    def test_lowerSection(self):
        data = [1,1,1,1,1] # yahtzee
        actual = lowerSection(data)
        self.assertTrue(50, actual)
        
        data = [1,2,3,4,5] # large straight
        actual = lowerSection(data)
        self.assertTrue(40, actual)

        data = [3,2,3,4,5] # small straight
        actual = lowerSection(data)
        self.assertTrue(30, actual)

        data = [2,2,3,3,3] # full house
        actual = lowerSection(data)
        self.assertTrue(30, actual)

        data = [2,3,3,3,3] # four kind
        actual = lowerSection(data)
        self.assertTrue(14, actual)

        data = [2,6,3,3,3] # three kind
        actual = lowerSection(data)
        self.assertTrue(17, actual)
