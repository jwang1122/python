import random

min = 1
max = 6

players = []
while True:
    player = input("Enter player name: ")
    players.append([player,0])
    more = input("More player? (y/n) ")
    if more=='n':
        break

roll_again = "yes"
while roll_again == "yes" or roll_again == "y":
    for player in players:
        bit = input(f"{player[0]}, what is your guess? (large/small)")
        player[1] = bit
    print("Rolling the dices...")
    print("The values are....")
    dice1 = random.randint(min, max)
    dice2 = random.randint(min, max)
    dice3 = random.randint(min, max)
    if (dice1+dice2+dice3 >= 9):
        print(f"{dice1}, {dice2}, {dice3} is large.")
    else:
        print(f"{dice1}, {dice2}, {dice3} is small.")
        
    roll_again = input("Roll the dices again?")

print("Result: ")

