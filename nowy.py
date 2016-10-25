from unittest import TestCase

from program import fizz_buzz_answer, for_function


class FizzBuzzTests(TestCase):
    def test_for_34_return_34(self):
        answer = fizz_buzz_answer(34)
        self.assertEqual("34", answer)

    def test_for_3_return_Fizz(self):
        answer = fizz_buzz_answer(3)
        self.assertEqual("Fizz", answer)

    def test_for_5_resturn_Buzz(self):
        answer = fizz_buzz_answer(5)
        self.assertEqual("Buzz", answer)

    def test_for_6_return_Fizz(self):
        answer = fizz_buzz_answer(6)
        self.assertEqual("Fizz", answer)

    def test_for_30_return_FizzBuzz(self):
        answer = fizz_buzz_answer(30)
        self.assertEqual("FizzBuzz", answer)

    def test_for_first_3_numbers(self):
        answer1 = for_function(3)
        self.assertEqual("1,2,Fizz", answer1)