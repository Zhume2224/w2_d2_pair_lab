import unittest
from src.coffee_shop import CoffeeShop
from src.drink import Drink
from src.customer import Customer




class TestCoffeeShop(unittest.TestCase):
    def setUp(self):
        self.coffee_shop1=CoffeeShop('Winnie',10)
        self.coffee_shop2 = CoffeeShop("Costa", 100)

        self.customer1=Customer("Jill", 10, 15)
        self.customer1.energy=30

        self.customer2=Customer("Nina", 50, 30)


        self.drink1=Drink('latte',3)

    def test_sell_drink(self):
        self.coffee_shop1.sell_drink(self.drink1, self.customer1)
        self.assertEqual(13,self.coffee_shop1.till)
        self.assertEqual(7, self.customer1.wallet)

    # def test_check_age(self):
    def test_check_if_old_enough(self):
        is_old_engough = self.coffee_shop2.old_enough(self.customer1)   # False 
        self.assertEqual(False, is_old_engough)

    def test_can_sell_drink(self):
        low_energy=self.coffee_shop1.have_low_energy(self.customer1)#-->note: this means using data in this class setUp area to test have_low_energy() function works or not in coffee_shop.py
        self.assertEqual(False,low_energy)



