from tkinter import *
from PIL import ImageTk # Pillow module
import random

class BaseWindow:
    root = Tk()
    def __init__(self):
        self.root.title("Blackjack Game")
        self.root.geometry("1024x768") # Super VGA monitor
        self.root.iconbitmap("src/images/blackjack.ico")
        self.buildWidgets()
        self.root.mainloop()
    
    def buildWidgets(self):
        pass

if __name__ == '__main__':
    BaseWindow()