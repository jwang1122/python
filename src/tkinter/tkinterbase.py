from tkinter import *

class TkinterBase:
    root = Tk()
    def __init__(self):
        self.root.title("Tkinter Window")
        self.root.geometry("1024x768")
        self.buildWidget()
        self.root.mainloop()

    def buildWidget(self): # declare a function without implementation
        pass # depends on subclass to implement it
 
if __name__ == '__main__':
   TkinterBase() 