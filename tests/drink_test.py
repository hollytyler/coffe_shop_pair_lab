import unittest
from src.drink import Drink



class TestDrink(unittest.TestCase):

    def setUp(self):
        self.coffee = Drink("Black Coffee", 3.90)

    def test_drink_has_name(self):
        self.assertEqual("Black Coffee", self.coffee.name)

    def test_drink_has_price(self):
        self.assertEqual(3.90, self.coffee.price)