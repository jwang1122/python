"""
Understand pake() function for Widget
"""
from tkinter import *
from tkinter import font

root = Tk()
root.title("My First Frame")
root.geometry("640x480")
root.iconbitmap("src/images/blackjack.ico")


label = Label(root, text="Welcome to Tkinter.", bg='yellow')
label.pack(fill=BOTH)
font1 = font.Font(family='Aerial bold', size='30')
def showMessage():
    print("I am clicked...")
#Button(root, text="Click Me", command=showMessage, fg='white', bg="#611A43", font=font1).pack(fill=BOTH, expand=1)
#Button(root, text="Click Me", command=showMessage, fg='white', bg="#611A43", font=font1).pack()
#Button(root, text="Click Me", command=showMessage, fg='white', bg="#611A43", font=font1).pack(fill=Y, expand=1)
Button(root, text="Click Me", command=showMessage, fg='white', bg="#611A43", font=font1).pack(side=BOTTOM)



root.mainloop()