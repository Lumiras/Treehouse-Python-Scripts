from combat import Combat
import random

COLORS = ['yellow', 'red', 'blue', 'orange', 'white', 'black']
WEAPONS = ['sword', 'halberd', 'mace', 'axe', 'bow and arrow', 'unarmed']

class Monster(Combat):
    min_hp = 1
    max_hp = 10
    min_exp = 1
    max_exp = 10
    weapon = 'sword'
    sound = 'raaar'


    def __init__(self, **kwargs):
        self.hp = random.randint(self.min_hp, self.max_hp)
        self.exp = random.randint(self.min_exp, self.max_exp)
        self.weapon     = random.choice(WEAPONS)
        self.color      = random.choice(COLORS)

        for key, value in kwargs.items():
            setattr(self, key, value)


    def battlecry(self):
        return self.sound.upper()

    def __str__(self):
        return '{} {}, HP: {}, XP: {}, wielding a {}'.format(self.color.title(), self.__class__.__name__, self.hp, self.exp, self.weapon)
class Goblin(Monster):
    max_hp = 5
    max_exp = 5
    sound = 'grrrgle'

class Troll(Monster):
    min_hp = 4
    max_hp = 15
    max_exp = 20
    sound = "You've entered my kingdom! Prepare to die!"

class Dragon(Monster):
    min_hp = 50
    max_hp = 100
    min_exp = 50
    max_exp = 100
    sound = "raaaaaaaaarrrrrrrrrk!"
