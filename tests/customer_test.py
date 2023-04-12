import unittest
from src.customer import Customer
from src.drink import Drink
from src.coffee_shop import CoffeeShop



class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer1=Customer('Jennifer',10, 26)
        self.customer2=Customer('Zhu',20, 25)

    def test_has_name(self):
        self.assertEqual('Zhu', self.customer2.name)

    def test_add_caffeine_level(self):
        customer = Customer("Gill", 12, 44)
        customer.energy = 0
        drink1 = Drink('Tea', 2.50)
        drink1.caffeine_level = 2
        self.assertEqual(2,customer.add_caffeine_level(drink1.caffeine_level))

