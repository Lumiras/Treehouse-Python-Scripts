```
#Find Cost of Tile to Cover W x H Floor - Calculate the total cost of tile it would take to cover a floor plan of width and height, using a cost entered by the user.

def tile_calc(length, width, type):
    user_length = int(length)
    user_width = int(width)
    tile = type.lower()
    price = 0
    if tile == 'slate':
        price = 10
    elif tile == 'limestone':
        price = 12
    elif tile == 'quartz':
        price = 20
    elif tile == 'marble':
        price = 55
    else:
        price = 10
        print("That's not a valid type of tile, we'll just use a price of $10 a square foot for now")
    return (user_length * user_width) * price
    
length = input("What is the length of the room (in feet)?")
width = input("What is the width of the room (in feet)?")
type = input("What kind of tile will you be using, slate, limestone, quartz, or marble?")

print("Your total is: $" + str(tile_calc(length, width, type)))
