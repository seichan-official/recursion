import random

number = random.randint(1,10)
guess = None

while guess != number:
    guess = input("guess a number between 1 and 10: ")
    guess = int(guess)
    
    if guess == number:
        print("You win!")
        break
    
    else:
        print("You lose")