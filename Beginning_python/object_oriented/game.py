import sys

from character import Character
from monster import Dragon
from monster import Troll
from monster import Goblin

class Game:
    def setup(self):
        self.player = Character()
        self.monsters = [
            Goblin(),
            Troll(),
            Dragon()
            ]
        self.monster = self.get_next_monster()

    def get_next_monster(self):
        try:
            return self.monsters.pop(0)
        except IndexError:
            return None

    def monster_turn(self):
        #see if monster attacks
        if self.monster.attack():
            #if so, tell player
            print("The {} attacks!".format(self.monster))
            #check if player wants to dodge
            trydodge = input("Do you want to try to dodge? Y/N").lower()
                #if so, see if dodge suceeds
            if trydodge == 'y':
                if self.player.dodge():
                    #if so, move on.org
                    print("you dodged the monster!")
            #if not, -1 hp
                else:
                    print("You got hit!")
                    self.player.hp -= 1
            else:
                print("{} hit you for 1 point!".format(self.monster))
                self.player.hp -= 1
        #if monster does not attack, tell player
        else:
            print("The {} misses! You're lucky!".format(self.monster))

    def player_turn(self):
        #let player attack, rest, or quit
        choice = input("Do you want to [A]ttack, [R]est, or [Q]uit?").lower()
        #if attack
        if choice == 'a':
            print("You attack the {}".format(self.monster))
            #see if attack succeeds
            if self.player.attack():
                #if so, see if monster dodges
                if self.monster.dodge():
                    #if dodged, print that
                    print("The monster dodged your attack!")
                #if not dodged, subtract HP from monster
                else:
                    print("You hit the {}!".format(self.monster))
                    self.monster.hp -= 1
            #if attack fails, tell player
            else:
                print("your attack failed!")
        #if rest
        elif choice == 'r':
            self.player.rest()
        #if quit
        elif choice == 'q':
            sys.exit()
        else:
            #run this method again
            print("That's not a valid option")
            self.player_turn()

    def cleanup(self):
        if self.monster.hp <= 0:
            #add exp to player
            self.player.exp += self.monster.exp
            #print congrats message
            print("Congratulations! You slayed the monster!")
            #get new monster
            self.player.levelup()
            self.monster = self.get_next_monster()

    def __init__(self):
        self.setup()
        while self.player.hp and (self.monster or self.monsters):
            print('\n' + '='*20)
            print (self.player)
            self.monster_turn()
            print('-'*20)
            self.player_turn()
            print('-'*20)
            self.cleanup()
            print('\n' + '='*20)
        if self.player.hp:
            print("You win!")
        elif self.monsters or self.monster:
            print("You lose!")
        sys.exit()

Game()
