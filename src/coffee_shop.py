class CoffeeShop:
    def __init__(self, name, till):
        self.name=name
        self.till=till
        self.drinks=['Mocha', 'Latte', 'Hot Chocolate', 'Tea']

    def sell_drink(self,drink_to_sell, customer_buying_drink):
        self.till+=drink_to_sell.price
        customer_buying_drink.wallet -= drink_to_sell.price
        return self.till
    
    def check_age(self, customer):
        if customer.age >= 16:
            return True
        else:
            return False
            print("You are too young")
        