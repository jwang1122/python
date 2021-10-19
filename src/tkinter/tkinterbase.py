from tkinter import *

class TkinterBase:
    def __init__(self):
        self.root = Tk()
        self.root.title("Tkinter Window")
        self.root.geometry("640x480")
        self.buildWidget()
        self.root.mainloop()

    def buildWidget(self): # declare a function without implementation
        pass # depends on subclass to implement it
 
if __name__ == '__main__':
   TkinterBase() 