
class Customer:
    def __init__(self,name,wallet, input_age):
        self.name=name
        self.wallet=wallet
        self.age = input_age
        self.energy = 0

    def add_caffeine_level(self,drink):
        
        self.energy += drink
        return self.energy


    # def can_buy_drink(self,drink_of_choice):

    #     if self.customer.wallet>=drink_of_choice.price:
    #         return True

    