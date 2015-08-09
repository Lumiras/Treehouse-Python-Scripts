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

# print(re.findall(r'''
#     \b@[-\w\d.]*    #find word boundary
#     [^gov\t]+
#     \b
#     ''', data, re.VERBOSE|re.I))
#
# print(re.findall(r"""
#     \b[-\w]*, #find word boundary, 1+ hyphens or chars and a comma
#     \s #find one whitespace
#     [-\w ]+ #one or more hyphens and characters and explicit spaces
#     [^\t\n] #ignore tabs and newlines
# """, data, re.X))

line=(re.compile(r'''
    ^(?P<name>(?P<last>[-\w ]*),\s(?P<first>[-\w ]+))\t #last and first names
    (?P<email>[-\w\d.+]+@[-\w\d.]+)\t #email
    (?P<phone>\(?\d{3}\)?-?\s?\d{3}-\d{4})?\t #phone numbers
    (?P<job>[\w\s]+,\s[\w\s.]+)\t? #job and company
    (?P<twitter>@[\w\d]+)?$ #twitter
''', re.X|re.M))

print(re.search(line, data).groupdict())
print(line.search(data).groupdict())
for match in line.finditer(data):
    print(match.group('name'))
    print(match.group('email'))
    print(match.group('phone'))
    print(match.group('twitter'))
    print("\n")

for match in line.finditer(data):
    print('{first} {last} <{email}>'.format(**match.groupdict()))
