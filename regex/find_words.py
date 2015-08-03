import re

def find_words(count,string):
    return re.findall(r'\b\w{'+str(count)+'}\b', string) #<-- cast count as string

print(find_words(4, "Four words are four and this four is four and fuck and four supermanisaghost five all the four letter words"))
