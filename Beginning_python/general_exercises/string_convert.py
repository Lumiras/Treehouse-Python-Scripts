import random
char_name = input("What is your name? ")
char_class = input("What is your class? ")
char_str = random.randrange(1, 18)
char_int = random.randrange(1, 18)
char_dex = random.randrange(1, 18)

print("Your name is {}, you are a brave {}. You have {} strength, {} intelligence, and {} dexterity. You are feared.".format(char_name, char_class, char_str, char_int, char_dex))