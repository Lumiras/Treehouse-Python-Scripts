dicts = [
    {'name' : 'August',
     'food' : 'Pretzels'},
    {'name' : 'Traci',
     'food' : 'Baskin Robbins'},
    {'name' : 'Cake Boss (Cake Boss)',
     'food' : 'Cake'},
    {'name' : 'Marissa',
     'food' : 'That thing where you take two DiGiorno pizzas and put cream cheese in the middle of them'},
    {'name' : 'Dalton',
     'food' : 'A hole in the ground, but that is not for food'}
]

string = "Hi, my name is {name}. My favorite food is {food}"

def string_factory(dicts, string):
    new_strings = []
    for items in dicts:
        new_dict = items
        new_strings.append(string.format(**new_dict))
    return new_strings

print(string_factory(dicts, string))
