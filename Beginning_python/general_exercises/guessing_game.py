import random
rando = random.randint(1, 10)
guesses = 1

while True:
    answer = int(input("Guess a number between 1 and 10: "))

    print("You have tried to guess the number {} times".format(guesses))

    if guesses > 4:
        print("You've tried to guess too many times. You lose")
        print("The correct number was {}".format(rando))
        break

    if answer < rando:
        print("Sorry, {} is too low. Guess again".format(answer))
        guesses = guesses + 1
        continue
    elif answer > rando:
        print("Sorry, {} is too high. Guess again".format(answer))
        guesses = guesses + 1
        continue
    else:
        print("Congrats, you guessed {}, and that was the number I guessed too!".format(answer))
        print("It only took you {} tries to get it!".format(guesses))
        break
