import random

# number of guesses (lower to increase difficulty)

a = 6

# Generates random number

magicNumber = random.randrange(1, 100)

# Welcom screen
def intro():
    print("\nWelcome to the world's greatest game, NUMBER WARS!!!")
    print("If you can guess the number I am thinking of in", a, "guesses,")
    print('then tomorrow, you will find the love of your life!\n')
    print("I'm thinking of a number between 1 and 100! ")
    print("May the odds be ever in your favor...")

# You guessed incorrectly, but have additional guesses
def guess_again(guess):
    if guess > magicNumber:
        print("Too high, Try again")
    elif guess < magicNumber:
        print("Too low, try again!")

 # You won on the last guess
def last_guess_win(guessnum):
    print("\nI'm not going to lie, I was pretty worried for a second..")
    print("You have barely skidded by with exactly", guessnum, "guesses!")
    print("\nMy number was", magicNumber)
    print("\nCongratulations, you will not die alone!")

# You won before the last guess
def win_before_last_guess(guessnum):
    print("\nOMG!!! YOU HAVE DONE THE IMPOSSIBLE")
    print("You have guessed my number in", guessnum, "tries!")
    print("\nMy number was", magicNumber)
    print("\nCongratulations, you will not die alone!")

# You guessed incorrectly, and you are out of guesses
def you_lose():
    print("\nDamn.. I REALLY hate to be the one to break this news to you..")
    print("But in all fairness, you knew the risk going into this...")
    print("\nMy number was", magicNumber)
    print("\nYou will never find love... :( ")


def main():
    intro()
    guessnum = 0

    # Sets counter that determines success or failure

    for i in range(1, a + 1, 1):
        guessnum = guessnum + 1
        guess = int(input("\n--> "))     

        
        if guess is magicNumber and i is a:
            last_guess_win(guessnum)
            break
        
        
        elif guess is magicNumber:
            win_before_last_guess(guessnum)
            break       

            
        elif guess is not magicNumber and i < a:
            guess_again(guess)
        
        
        else:
            you_lose()

    exit(0)


# Calls all functions

if __name__ == '__main__':
    main()
