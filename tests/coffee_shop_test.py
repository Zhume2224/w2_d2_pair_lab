import unittest
from src.coffee_shop import CoffeeShop

class TestCoffeeShop(unittest.TestCase):
    def setUp(self):
        self.coffee_shop=CoffeeShop(self,'Winnie',1000)

