import random

number = random.randint(1,10)
guess = None
attempts = 0
max_attempts = 5

while guess != number:
    guess = input(f"Attempt {attempts + 1} of {max_attempts}: Guess a number between 1 and 10: ")
    guess = int(guess)
    attempts += 1
    if guess == number:
        print(f"You win! It took you {attempts} attempts")
        break
    else:
        print("You lose")
    if attempts == max_attempts:
        print(f"You've used all {max_attempts} attempts. The correct number was {number}.")
