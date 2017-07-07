import random

# number of guesses (lower to increase difficulty)

a = 6

# Prints initial welcome screen

def intro():
    print("\nWelcome to the world's greatest game, NUMBER WARS!!!")
    print("If you can guess the number I am thinking of in", a, "guesses,")
    print('then tomorrow, you will find the love of your life!\n')


# Generates random number

magicNumber = random.randrange(1, 100)


# All The Good Stuff

def numGame(magicNumber):
    print("I'm thinking of a number between 1 and 100! ")
    guess = int(input("May the odds be ever in your favor...\n"))
    guessnum = 0

    # Sets counter that determines success or failure

    for i in range(1, a + 1, 1):

        # You won on the last guess

        if guess is magicNumber and i is a:
            guessnum = guessnum + 1
            print("\nI'm not going to lie, I was pretty worried for a second..")
            print("You have barely skidded by with exactly", guessnum, "guesses!")
            print("\nMy number was", magicNumber)
            print("\nCongratulations, you will not die alone!")
            break

        # You won before the last guess

        elif guess is magicNumber:
            guessnum = guessnum + 1
            print("\nOMG!!! YOU HAVE DONE THE IMPOSSIBLE")
            print("You have guessed my number in", guessnum, "tries!")
            print("\nMy number was", magicNumber)
            print("\nCongratulations, you will not die alone!")
            break

        # You guessed incorrectly, but have additional guesses

        elif guess is not magicNumber and i < a:
            if guess > magicNumber:
                guess = int(input("Too high, try again!\n"))
            elif guess < magicNumber:
                guess = int(input("Too low, try again!\n"))
            guessnum = guessnum + 1

        # You guessed incorrectly, and you are out of guesses

        else:
            print("\nDamn.. I REALLY hate to be the one to break this news to you..")
            print("But in all fairness, you knew the risk going into this...")
            print("\nMy number was", magicNumber)
            print("\nYou will never find love... :( ")


# Calls all functions

intro()
numGame(magicNumber)
