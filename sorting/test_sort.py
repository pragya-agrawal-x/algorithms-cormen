import unittest
from sorting.sort import *

# For file to be discovered by python -m unittest discover;
# file name should be a legal Python identifier and should start with test
# Also function name should start with test

class SortTest(unittest.TestCase):
    def test_insertion_sort(self):
        input_sequence = [999, 888, 777, 666, 555, 444, 333, 222, 111, 0]
        sort_by_insertion_sort(input_sequence)
        expected_sorted_sequence = [0, 111, 222, 333, 444, 555, 666, 777, 888, 999]
        self.assertEqual(input_sequence, expected_sorted_sequence)
