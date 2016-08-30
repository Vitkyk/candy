__author__ = 'vitkyk'
import unittest
from main import multi_xor, find_answer, calculate


class TestStringMethods(unittest.TestCase):

    def test_single_multi_xor(self):
        self.assertEqual(multi_xor([7]), 7)

    def test_normal_multi_xor(self):
        self.assertEqual(multi_xor([7, 3, 8, 9]), 5)

    def test_find_answer(self):
        self.assertEqual(find_answer([1, 2, 3, 4, 5]), 14)

    def test_single_calculate(self):
        self.assertEqual(calculate([1]), "NO")

    def test_unsuccessful_calculate(self):
        self.assertEqual(calculate([1, 2, 3, 4, 5]), "NO")

    def test_successful_calculate(self):
        self.assertEqual(calculate([3, 5, 6]), 11)