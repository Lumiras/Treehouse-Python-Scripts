shopping_list = []

def clear_list():
    confirm = input("Are you sure you want to completely clear the list?\nThere is no way to undo this!\nType YES to confirm ")
    if confirm == 'YES':
        del shopping_list[:]

def move_item(idx, mov):
    index = idx - 1
    item = shopping_list.pop(index - 1)
    shopping_list.insert(mov, item)

def remove_item(idx):
    index = idx - 1
    item = shopping_list.pop(index)
    print("Removed {} ".format(item))

def show_help():
    print("\nSeparate each item with a comma")
    print("Type DONE to quit\nType SHOW to see the current list\nType HELP to get this message\nType REMOVE to delete an item")

def show_list():
    if len(shopping_list) > 0:
        count = 1
        for item in shopping_list:
            print("{} -> {}".format(count, item))
            count += 1
    else:
        print("\nYour shopping list is currently empty")


def prompt():
    print("\nGive me a list of things you want to shop for: ")

show_help()

while True:
    prompt()
    new_stuff = input(">>")

    if new_stuff == "DONE":
        print("\nHere's your list:")
        show_list()
        break
    elif new_stuff == "HELP":
        show_help()
        continue
    elif new_stuff == "SHOW":
        show_list()
        continue
    elif new_stuff == "REMOVE":
        show_list()
        idx = input("Which item do you want to remove? ")
        remove_item(int(idx))
        continue
    elif new_stuff == "MOVE":
        show_list()
        idx = input("Which item do you want to move? ")
        mov = input("Where do you want to move the item? ")
        move_item(int(idx), int(mov))
    elif new_stuff == "CLEAR":
        clear_list()
    else:
        new_list = new_stuff.split(",")
        index = input("Add this at a certain spot? Press ENTER to insert at the end of the list "
        "\nor give me a number to place it at a certain spot. You currently have {} items in your list:  ".format(len(shopping_list)))
        if index:
            spot = int(index)-1
            for item in new_list:
                shopping_list.insert(spot, item.strip())
                spot += 1
        else:
            for item in new_list:
                shopping_list.append(item.strip())
