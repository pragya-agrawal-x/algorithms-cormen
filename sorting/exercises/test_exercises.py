import unittest
from sorting.exercises.exercise_2_1_2 import *


class ExerciseTest(unittest.TestCase):
    def test_exercise_2_1_2(self):
        input_sequence = [0, 111, 222, 333, 444, 555, 666, 777, 888, 999]
        insertion_sort_descending(input_sequence)
        expected_sorted_sequence = [999, 888, 777, 666, 555, 444, 333, 222, 111, 0]
        self.assertEqual(input_sequence, expected_sorted_sequence)
