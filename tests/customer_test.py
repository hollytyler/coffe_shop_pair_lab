import unittest
from src.customer import Customer
from src.drink import Drink

class TestCustomer(unittest.TestCase):

    def setUp(self):
        self.customer = Customer("Holly", 10)
        self.mocha = Drink("Mocha", 3)
        self.latte = Drink("Latte", 4)
        self.drinks = [self.mocha, self.latte]

    def test_customer_has_name(self):
        self.assertEqual("Holly", self.customer.name)

    def test_customer_wallet(self):
        self.assertEqual(10, self.customer.wallet)

    def test_customer_purchase(self):
        self