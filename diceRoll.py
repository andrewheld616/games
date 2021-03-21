import random

# a simple game that simulates the roll of a dice, prints the result and loops should the user choose to
while True:
    print(''' 1. Roll the dice                 2. exit       ''')
    user = int(input("What do you want to do\n"))
    if user==1:
        number = random.randint(1,6)
        print("You rolled: ")
        print(number)
    else:
        break
