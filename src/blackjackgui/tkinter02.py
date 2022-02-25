from tkinter import *

root = Tk()
root.title("My First Frame")
root.geometry("640x480")
root.iconbitmap("src/images/blackjack.ico")

def showMessage():
    print("I am clicked...")
    
Button(root, text="Click Me", command=showMessage).pack()

root.mainloop()