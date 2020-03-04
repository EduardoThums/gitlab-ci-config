from unittest import TestCase

from calculator_package.calculator import sum_two_numbers


class TestCalculator(TestCase):

    def test_sum_two_numbers(self):
        number_one = 1
        number_two = 1

        sum_result = sum_two_numbers(number_one, number_two)

        self.assertEqual(2, sum_result)
