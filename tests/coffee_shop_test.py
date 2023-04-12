import unittest
from src.coffee_shop import CoffeeShop
from src.drink import Drink
from src.customer import Customer






class TestCoffeeShop(unittest.TestCase):
    def setUp(self):
        self.coffee_shop1=CoffeeShop('Winnie',10)

    def test_sell_drink(self):
        drink1=Drink('latte',3)
        # drink=Drink.price
        customer1=Customer('Joe',10)
        self.coffee_shop1.sell_drink(drink1, customer1)
        self.assertEqual(13,self.coffee_shop1.till)
        self.assertEqual(7, customer1.wallet)

