my_phrase = "this is this kind of string and this kind of string has this kind of repetitive words so that this string will produce matches and this kind of match will provide data to match us with the correct things that this string is trying to accomplish and this will make sure that our data is correct and if we match things up the data will look better and we will all be happier all because this string and this function and this language was doing its job"

def word_count(phrase):
    collection = {}
    for word in phrase.split():
        if word in collection:
            collection[word] += 1
        else:
            collection[word] = 1
    return collection

print(word_count(my_phrase))
