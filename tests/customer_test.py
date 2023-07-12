import unittest
from src.customer import Customer

class TestCustomer(unittest.TestCase):

    def setUp(self):
        self.customer = Customer("Holly", 10)

    def test_customer_has_name(self):
        self.assertEqual("Holly", self.customer.name)

    def test_customer_wallet(self):
        self.assertEqual(10, self.customer.wallet)