from random import *

number = input("Enter a number between (1-100)")
guess = int(number)

rand = randint(1, 100)

while(guess!=rand):
    if guess>rand:
        print("your guess is greater.")
    if guess<rand:
        print("your guess is less")
    guess = int(input("Try it again: "))
print("You got it!")