import random

# Generate a random number between 1 and 25
secret_number = random.randint(1, 25)

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 25.")
print("You have 3 attempts to guess it.")

attempts = 3

for attempt in range(1, attempts + 1):
    try:
        guess = int(input(f"Attempt {attempt}: Enter your guess: "))
        if guess == secret_number:
            print("Congratulations! You guessed the number correctly.")
            break
        else:
            if guess > secret_number:
                print("Too high.")
            else:
                print("Too low.")
    except ValueError:
        print("Invalid input. Please enter a number.")

if guess != secret_number:
    print(f"Sorry, you've used all attempts. The number was {secret_number}.")
