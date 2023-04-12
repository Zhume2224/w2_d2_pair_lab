import unittest
from src.customer import Customer
from src.drink import Drink
from src.coffee_shop import CoffeeShop



class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer1=Customer('Jennifer',10)
        self.customer2=Customer('Zhu',20)

    def test_has_name(self):
        self.assertEqual('Zhu', self.customer2.name)

