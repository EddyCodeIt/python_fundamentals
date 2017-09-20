# library for generating random numbers for security purposes
import secrets

range = int(input("Pick a guessing range (0 - 7/10/13/22/...): ")) + 1
#range = 100
numOfGuesses = 0 # start of a game

def guessing_game(range):
    # Generate a number to guess based on a range.
    # To generate a number, I've decided to check a secrets module in python libraries,
    # that provides access to the most secure source of randomness that your operating system provides
    # Ref.: https://docs.python.org/3/library/secrets.html#module-secrets
    guessIt = secrets.randbelow(range)
    print(guessIt)
    guessing = True # set to false to stop the game, indicates that number is guessed

    # run the loop until a write guessing flag is not False
    while(guessing):
        # Take a user input
        guess = int(input("Enter your guess number: "))
        # compare input to a generated value 
        if guess == guessIt:
            print(True) # print True to indicating that a guess is correct
            guessing = False # exit a loop
        else:
            print(False) # print False and go to next itteration

# Run a function
guessing_game(range)
print("Game over... ")