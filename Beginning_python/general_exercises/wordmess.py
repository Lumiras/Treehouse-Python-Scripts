capture = input("Write a sentence, and I'll provide some dumb facts about it: ")

phrase = capture.split()
phrase_length = len(phrase)
second_word = phrase[1]
fifth_word = phrase[4]
jumbled = phrase.reverse()

print("your phrase is {} words long. The second word is {}, the fifth word is {}. If I reverse it, it reads {}".format(phrase_length, second_word, fifth_word, jumbled))
