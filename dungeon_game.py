#Create a game with a 2-dimensional map.
#Place the player, a door, and a monster into random spots in your map.
#Let the player move around in the map and, after each move, tell them if they've found the door or the monster.
#If they find either the game is over. The door is the win condition, the monster is the lose condition.
import random
my_list = list(range(101))
print(random.choice(my_list))

COORDS =    [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4),
             (1, 0), (1, 1), (1, 2), (1, 3), (1, 4),
             (2, 0), (2, 1), (2, 2), (2, 3), (2, 4),
             (3, 0), (3, 1), (3, 2), (3, 3), (3, 4),
             (4, 0), (4, 1), (4, 2), (4, 3), (4, 4)]
print(random.choice(my_coords))

# def nchoices(ite, num):
#     results = []
#     for index in range(num):
#         pick = random.choice(ite)
#         results.append(pick)
#     return results

def get_locations():
    monster = random.choice(CELLS)
    door = random.choice(CELLS)
    player = random.choice(CELLS)
    #if monster, door or start are the same, re-roll
    if monster == door or monster == start or door == start:
        return get_locations()

    return monster, door, player

def move_player(player, move):
    #get current loc
    #if move is left,  y - 1
    #if move is right, y + 1
    #if move is up,    x - 1
    #if move is down,  x + 1

def get_moves(player):
    MOVES = ['LEFT', 'RIGHT', 'UP', 'DOWN']
    #if player's y is 0, remove left
    #if player's x is 0, remove up
    #if player's y is 4, remove right
    #if player's x is 4, remove down
    return MOVES

monster, door, player = get_locations()

while True:
    print("Welcome to my dungeon!")
    print("You are currently in room {}".format(player))
    print("You can move {}") #fill with available moves
    print("Enter QUIT to quit")

    moves = get_moves(player)

    move = input("> ")
    move = move.upper()

    if move == 'QUIT':
        break

    #if good move, change player pos
    #if bad move, don't change
    #if new player pos is door, they win
    #if new player pos is monster, they lose
    #otherwise, continue
