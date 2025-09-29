import random

# Pick a random number between 1 and 10

secret = random.randint(1, 10)
guess = None 

print("🎲 Welcome to the Guessing Game!")
print("I'm thinking of a number between 1 and 10.")

# Keep asking until correct

while guess != secret:
    guess = int(input("Enter your guess: "))

    if guess < secret:
        print("Too low! try again.")
    elif guess > secret:
        print("Too high! Try again.")
    else:
        print("🎉 Correct! The number was", secret)