import random
class Hero:
    """
    This is our hero blueprint.
    
    O=('-'Q)

    Attributes:
        name: The name of our adventurer.
        hp: The current health value.
        strength: The amount of damage the hero can deal.
        (Bonus) defence: A hero's ability to reduce incoming damage.
        (Bonus) special_ability: A unique ability the hero can use.
    """
    
    def __init__(self, name):
        self.name = name
        self.health = 300
        self.attack_power = random.randint(20, 40)
    

    def strike(self):
        return random.randint(15, self.attack_power)
    
    def receive_damage(self, damage):
        if (self.health - damage) >= 0:
            self.health -= damage
        else: 
            self.health = 0
            print(f"Hero has been defeated")
        
    
    def is_alive(self):
        if self.health > 0:
            alive = True
        else: 
            alive = False
        return alive