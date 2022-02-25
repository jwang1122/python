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
text1 = StringVar()
text1.set("Hello World!")
label1 = Label(root, textvariable=text1, font=font1) # Demand Driven Development
label1.pack()

flag = True
def showMessage():
    global flag
    if flag:
        text1.set("The button is clicked...")
    else:
        text1.set("Hello TKinter!")
    flag = not flag 

Button(root, text="Toggle Messages", command=showMessage, fg='white', bg="#611A43", font=font1).pack(side=BOTTOM)



root.mainloop()