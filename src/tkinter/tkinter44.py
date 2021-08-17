import tkinter as tk
from PIL import Image, ImageTk
import random

class Player:
    def __init__(self, name):
        self.name = name
        self.cardX = 70
        self.cardY = 100

    def __repr__(self):
        return name
        
    def getCardX(self):
        self.cardX += 30
        return self.cardX
    
    def getCardY(self):
        return self.cardY

class Dealer(Player):
    def __init__(self):
        self.name = "Dealer"

class MyFrame():
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("My Blackjack Card Game")
        self.root.geometry('1240x768')
        self.root.grid()
        self.create_widgets()
        self.playerList = []

    def create_widgets(self):
        self.dealBtn = tk.Button(self.root, text="Deal Card", command=self.deal)
        self.dealBtn.place(x=10, y=20)

    def deal(self):
        print("deal card...")

    def addPlayer(self):
        while True:
            answer = input("More player? (y/n) ")
            if answer.lower() == 'n':
                break
            name = input("Enter player's name: ")
            self.playerList.append(Player(name))

if __name__ == '__main__':
    game = MyFrame()
    MyFrame.root.mainloop()