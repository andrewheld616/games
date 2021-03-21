import random

# a simple program that generates a random password of user input length from a series of possible characters
passlen = int(input("Enter the desired length of new password:   "))
s="abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
p = "".join(random.sample(s,passlen ))
print (p)