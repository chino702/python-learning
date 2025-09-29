import random # lets us use random numbers

# Pick a random number between 1 and 10
secret = random.randit(1, 10)

# Start with no guessing yet
guess = None

attempts = 0 # this will count how many tries the player makes

print("🎲 Welcome to the Guessing Game!")

print("I'm thinking of a number between 1 and 10.")

# Keep looping until the player guesses correctly
while guess != secret:

    # Ask for input
    guess = int(input("Enter your guess: "))

    # Add +1 to the counter each time a guess is made
    attempts += 1

    # Checks if guess is to high
    if guess > secret:
      print("Too high! Try again.")

    # Checks if guess is to low
    elif guess < secret:
       print("Too low! Try again.")

       # If neither, they must be correct
    else:
       print("🎉 Correct! The number was", secret)
       print("You guessed it in", attempts, "tries!")