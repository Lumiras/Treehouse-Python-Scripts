#Create a game with a 2-dimensional map.
#Place the player, a door, and a monster into random spots in your map.
#Let the player move around in the map and, after each move, tell them if they've found the door or the monster.
#If they find either the game is over. The door is the win condition, the monster is the lose condition.
import random
# my_list = list(range(101))
# print(random.choice(my_list))

CELLS =     [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4),
             (1, 0), (1, 1), (1, 2), (1, 3), (1, 4),
             (2, 0), (2, 1), (2, 2), (2, 3), (2, 4),
             (3, 0), (3, 1), (3, 2), (3, 3), (3, 4),
             (4, 0), (4, 1), (4, 2), (4, 3), (4, 4)]
# print(random.choice(my_coords))

# def nchoices(ite, num):
#     results = []
#     for index in range(num):
#         pick = random.choice(ite)
#         results.append(pick)
#     return results

print("Welcome to my dungeon!")

def get_locations():
    monster = random.choice(CELLS)
    door = random.choice(CELLS)
    player = random.choice(CELLS)
    #if monster, door or start are the same, re-roll
    if monster == door or monster == player or door == player:
        return get_locations()

    return monster, door, player

def move_player(player, move):
    x, y = player

    if move == 'LEFT':
        y -= 1
    elif move == 'RIGHT':
        y += 1
    elif move == 'UP':
        x -= 1
    elif move == 'DOWN':
        x += 1

    return x, y


def get_moves(player):
    moves = ['LEFT', 'RIGHT', 'UP', 'DOWN']
    if player[1] == 0:
        moves.remove('LEFT')
    if player[1] == 4:
        moves.remove('RIGHT')
    if player[0] == 0:
        moves.remove('UP')
    if player[0] == 4:
        moves.remove('DOWN')
    return moves

def draw_map(player):
    tile = '{}'

    for idx, cell in enumerate(CELLS):
        if idx in [1, 2, 3, 6, 7, 8, 11, 12, 13, 16, 17, 18, 21, 22, 23]:
            if cell == player:
                print(tile.format(' X '), end='')
            elif cell == door:
                print(tile.format(' D '), end='')
            elif cell == monster:
                print(tile.format(' M '), end='')
            else:
                print(tile.format(' _ '), end='')
        elif idx in [4, 9, 14, 19, 24]:
            if cell == player:
                print(tile.format(' X|\n'))
            elif cell == door:
                print(tile.format(' D|\n'))
            elif cell == monster:
                print(tile.format(' M|\n'))
            else:
                print(tile.format(' _|\n'))
        elif idx in [0, 5, 10, 15, 20]:
            if cell == player:
                print(tile.format('|X '), end='')
            elif cell == door:
                print(tile.format('|D '), end='')
            elif cell == monster:
                print(tile.format('|M '), end='')
            else:
                print(tile.format('|_ '), end='')


monster, door, player = get_locations()

while True:
    moves = get_moves(player)
    print("You are currently in room {}".format(player))
    draw_map(player)
    print("You can move {}".format(moves)) #fill with available moves
    print("Enter QUIT to quit")



    move = input("> ")
    move = move.upper()

    if move == 'QUIT':
        break

    #if good move, change player pos
    if move in moves:
        player = move_player(player, move)
    else:
        print("Walls are very hard. Stop walking into them")
        continue

    if player == door:
        print("You escaped!!!")
        break

    if player == monster:
        print("\n\nYou suffered the most horrible of fates.\n I can't even describe how horrible it was.\n It was so gross.\n Like, seriously, I could draw a picture of it...\n...but it would probably crash this computer.\nPlease, take my word for it.\n\n")
        break


    #if bad move, don't change
    #if new player pos is door, they win
    #if new player pos is monster, they lose
    #otherwise, continue
