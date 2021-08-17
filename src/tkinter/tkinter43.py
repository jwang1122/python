"""
deal cards in window
"""
import tkinter as tk
from PIL import Image, ImageTk
import random

class Card:
    suits = ["spade","club","diamond","heart"]
    faces = ["A",'2','3','4','5','6','7','8','9','10','J',"Q",'K']

    def __init__(self, face, suit):
        self.face = face
        self.suit = suit
    
    def __repr__(self):
        return '('+self.face+', '+self.suit+')'
    
    def getImage(self):
        filename = "images/"+self.suit+self.face+".gif"
        image = ImageTk.PhotoImage(file=filename)
        return image
    

def init():
    global root
    global frame
    global cards
    global x1,y1
    root = tk.Tk()
    root.geometry("1024x768")
    root.resizable(0, 0)
    root.title("tkinter42")
    frame = tk.Frame(root, width = 1024, height = 768)
    frame.grid()
    x1=130
    y1=100
    dealBut = tk.Button(root, text="Deal Card", command=deal).place(x=5, y=5)

    cards = [Card(face, suit) for face in Card.faces for suit in Card.suits]

def deal():
    global x1, y1
    index = random.randint(0,51)
    card = cards[index]
    img = card.getImage()
    label = tk.Label(frame)
    label.configure(image=img)
    label.image = img
    label.place(x=x1, y=y1)
    x1 += 30

if __name__ == '__main__':
    init()
    heartQ = ImageTk.PhotoImage(file="images/heartQ.gif")
    tk.Label(frame, image = heartQ).place(x=100, y=100)

    root.mainloop()