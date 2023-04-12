class Customer:
    def __init__(self,name,wallet):
        self.name=name
        self.wallet=wallet


    def can_buy_drink(self,drink_of_choice):

        if self.customer.wallet>=drink_of_choice.price:
            return True