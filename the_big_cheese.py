from enemy import Enemy
import random


class BigCheese(Enemy):
    def __init__(self, name):

        self.name = name
        self.attack_power = random.randint(20, 40)
        self.health = 300 

    def attack(self):
        if self.health < 50: 
            self.attack_power = random.randint(40, 75)
            print("The Big Cheese is a bit grumpy now")
        return self.attack_power



