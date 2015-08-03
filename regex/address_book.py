import re

names_file = open('names.txt', encoding='utf-8')
data = names_file.read()
names_file.close()

#print(re.search(r'\(\d\d\d\) \d\d\d-\d\d\d\d', data))   #dumb way of trying to find phone numbers

# print(re.search(r'\(?\d{3}\) \d{3}-\d{4}', data))    #better way of trying to find properly formatted phone numbers

# print(re.findall(r'\(?\d{3}\)?-?\s?\d{3}-\d{4}', data))

# print(re.findall(r'\w*, \w+', data))     #finds first instance of {word}, {word} in file

# print(re.findall(r'[-\w\d+.]+@[-\w\d.]+', data))
# print(re.findall(r'\b[trehous]{9}\b', data, re.I))

print(re.findall(r'''
    \b@[-\w\d.]*    #find word boundary
    [^gov\t]+
    \b
    ''', data, re.VERBOSE|re.I))
