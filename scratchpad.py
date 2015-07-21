# def say_hello():
#     print("Hello")
#
# say_hello()
#
# def add_to_two(num):
#     print(num + 2)
#
# add_to_two(4)
#
# def square(num):
#     return num * num
#
# square(5)

# my_string = "Hi! My name is {name} and I live in {state}, I am currently a {job}, and my favorite food is {food}. If I would have to pick one person to have dinner with, it would be {favper}, and I would eat {food} with them for sure. This paragraph is being filled in by {language} so don't get that excited that I'm spending much time on it. It's as simple as {bakedgood}"
# my_dict = {'name' : 'Sean', 'state' : 'Indiana', 'job': 'student', 'food': 'sushi', 'favper': 'Abraham Lincoln', 'language': 'Python', 'bakedgood': 'pie'}
#
# print(my_string.format(**my_dict))
#
# my_dict = {'name' : 'Sean', 'state' : 'Indiana', 'job': 'student', 'food': 'sushi', 'favper': 'Abraham Lincoln', 'language': 'Python', 'bakedgood': 'pie'}
#
# for value in my_dict.values():
#     print(value)

my_alphabet_list = list('abcdefghijklmnopqrstuvwxyz')

# count = 0
# for letter in my_alphabet_list:
#     print('{}: {}'.format(count, letter))
#     count += 1

for whateveriwantittobe in enumerate(my_alphabet_list):
    print('{} : {}'.format(*whateveriwantittobe))

dicts = {'name' : 'August', 'food' : 'Pretzels', 'hobbies' : 'Suicide', 'nationality' : 'German'}
for key, value in dicts.items():
    print('{} : {}'.format(key.title(), value))
