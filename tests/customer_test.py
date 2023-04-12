import unittest
from src.customer import Customer
from src.drink import Drink
from src.coffee_shop import CoffeeShop
from src.food import Food





class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer1=Customer('Jennifer',10, 26)
        self.customer1.energy=10

        self.customer2=Customer('Zhu',20, 25)
        self.food1=Food('burger',4,6)
    

    def test_has_name(self):
        self.assertEqual('Zhu', self.customer2.name)

    def test_customer_can_add_caffeine_level(self):
        customer = Customer("Gill", 12, 44)
        customer.energy = 0
        drink1 = Drink('Tea', 2.50)
        drink1.caffeine_level = 2
        # self.assertEqual(2,customer.add_caffeine_level(drink1.caffeine_level))
        self.assertEqual(2,customer.add_caffeine_level(drink1))


    def test_customer_can_reduce_rejuvenation_level(self):
       self.customer1.reduce_energy(self.food1)
       self.assertEqual(4, self.customer1.energy)


