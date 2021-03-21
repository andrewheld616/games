import random

number = random.randint(1,10)
for i in range(0,3):
    user = int(input("Guess the number between 1 and 10:    "))
    if user == number:
        print("Hurray!!")
        print(f"You guessed the right number: {number}")
        break

if user != number:
    print(f"Your guess was wrong. The number was {number}")