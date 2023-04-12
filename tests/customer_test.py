import unittest
from src.customer import Customer

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer1=Customer('Jennifer',10)
        self.customer2=Customer('Zhu',20)


    def test_can_buy_drink(self):
        drink1=Drink('latte',4)
        drink2=Drink('Flat White',3)
        
        self.assertEqual(True,self.can_buy_drink())