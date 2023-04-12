import unittest
from src.drink import Drink

class TestDrink(unittest.TestCase):
    def setUp(self):
        self.drink1=Drink('Flat White',3)
        self.drink2=Drink('Latte',4)