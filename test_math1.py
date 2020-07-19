import unittest
from math1 import *


class Test_Math1(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(3, 4), 7)
        self.assertEqual(add(3, (1, 3, 7, 9)), (4, 6, 10, 12))
        self.assertEqual(add((1, 3, 7, 9), 3), (4, 6, 10, 12))
        self.assertEqual(add([1, 3, 7, 9], 3), [4, 6, 10, 12])
        self.assertEqual(add(3, [1, 3, 7, 9]), [4, 6, 10, 12])
