
class Customer:
    def __init__(self,name,wallet, input_age):
        self.name=name
        self.wallet=wallet
        self.age = input_age
        self.energy = 0

    # def add_caffeine_level(self,drink):
        
    #     self.energy += drink
    #     return self.energy

    def add_caffeine_level(self,drink):
        
        self.energy += drink.caffeine_level
        return self.energy

    def reduce_energy(self,food):
        self.energy-=food.rejuvenation_level
        
    