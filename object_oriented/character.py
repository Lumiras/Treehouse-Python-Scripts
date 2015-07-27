import random
from combat import Combat
class Character(Combat):
    attack_limit = 10
    base_hp = 10
    exp = 0
    level = 1

    def attack(self):
        roll = random.randint(1, self.attack_limit)
        if self.weapon == 'sword':
            roll += 1
        elif self.weapon == 'axe':
            roll += 2
        return roll > 4

    def get_weapon(self):
        weapon_choice = input("Weapon ([S]word, [A]xe, [B]ow): ").lower()
        if weapon_choice == 's' or weapon_choice == 'sword':
            return 'sword'
        elif weapon_choice == 'a' or weapon_choice == 'axe':
            return 'axe'
        elif weapon_choice == 'b' or weapon_choice == 'bow':
            return 'bow'
        else:
            print("That's not a valid choice")
            return self.get_weapon()

    def __init__(self, **kwargs):
        self.name = input("What is your name?: ")
        self.weapon = self.get_weapon()
        for key, value in kwargs.items():
            setattr(self, key, value)
        self.hp = self.base_hp

    def __str__(self):
        return '{}, HP: {}, XP: {}, Weapon: {}'.format(self.name, self.hp, self.exp, self.weapon)

    def rest(self):
        if self.hp < self.base_hp:
            self.hp += 1

    def levelup(self):
        if self.exp > 0:
            self.level += 1
            print("Congratulations, you have reached level {}".format(self.level))
