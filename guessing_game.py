# library for generating random numbers for security purposes
import secrets

range = int(input("Pick a guessing range (0 - 7/10/13/22/...): ")) + 1

def guessing_game(range):
    # Generate a number to guess based on a range.
    # To generate a number, I've decided to check a secrets module in python libraries,
    # that provides access to the most secure source of randomness that your operating system provides
    # Ref.: https://docs.python.org/3/library/secrets.html#module-secrets
    guessIt = secrets.randbelow(range)

    numOfGuesses = 0 # start of a game

    print("(For sTesting)Number to be guessed: " + str(guessIt))
    prevGuess = range + 1 # add one just to get outside a range of guessing nums, 
                          # so that it would be possible to initialize variable and avoid a 0 bug
                          # since it's included in a guessing range.
    guessing = True # set to false to stop the game, indicates that number is guessed

    # run the loop until a write guessing flag is not False
    while(guessing):
        # Take a user input
        guess = int(input("Enter your guess number: "))

        # compare input to a generated value 
        if guess == guessIt:
            numOfGuesses += 1
            print(True) # print True to indicating that a guess is correct
            guessing = False # exit a loop

        else:
            if prevGuess != guess:
                numOfGuesses += 1
            prevGuess = guess
            print(False) # print False and go to next itteration
    return numOfGuesses
# Run a function

print("Game over... Attempts: " + str(guessing_game(range)))