from django.test import SimpleTestCase
from . import calc


class CalcTestCase(SimpleTestCase):
    def test_add_two_numbers(self):
        res = calc.add(5, 6)
        self.assertEqual(res, 11)

    def test_subtract_two_numbers(self):
        res = calc.subtract(4, 3)
        self.assertEqual(res, 1)
