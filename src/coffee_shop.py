class CoffeeShop:
    def __init__(self, name, till):
        self.name=name
        self.till=till
        self.drinks=['Mocha', 'Latte', 'Hot Chocolate', 'Tea']

    def sell_drink(self,drink_to_sell, customer_buying_drink):
        self.till+=drink_to_sell.price
        customer_buying_drink.wallet -= drink_to_sell.price
      
    
    def old_enough(self, customer):
        if customer.age >= 16:
            return True
        else:
            return False

    def have_low_energy(self,customer):
        if customer.energy<=20:
            return True
        else:
            return False

    
           
        