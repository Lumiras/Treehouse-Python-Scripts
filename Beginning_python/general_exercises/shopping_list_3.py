shopping_list = []

def show_help():
    print("\nSeparate each item with a comma")
    print("Type DONE to quit, SHOW to see the current list, and HELP to get this message")

def show_list():
    count = 1
    for item in shopping_list:
        print("{} -> {}".format(count, item))
        count += 1

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
    else:
        new_list = new_stuff.split(",")
        index = input("Add this at a certain spot? Press ENTER to insert at the end of the list"
        "\nor give me a number to place it at a certain spot. You currently have {} items in your list: ".format(len(shopping_list)))
        if index:
            spot = int(index)-1
            for item in new_list:
                shopping_list.insert(spot, item.strip())
                spot += 1
        else:
            for item in new_list:
                shopping_list.append(item.strip())
