from tkinter import *
from turtle import onclick

bg1 = '#FF0000'
rbl = []
def getSelected():
    bg1 = colorVar.get()
    root.configure(bg=bg1)
    lbl.configure(bg=bg1)
    for b in rbl:
        b.configure(bg=bg1)

root = Tk()
root.geometry("600x400")
root.title("Radio Button")
colorVar = StringVar()
colorVar.set('#FF0000')
topping = [
    ("blue", '#0000FF'),
    ("red", '#FF0000'),
    ("yellow", '#FFFF00'),
    ("cyan", '#00FFFF'),
    ("gray", "#888888")
]

for text, num in topping:
    b = Radiobutton(root, text=text, variable=colorVar, value=num, command=getSelected)
    b.pack()
    rbl.append(b)

lbl = Label(root, textvariable=colorVar, fg='#FFFFFF')
lbl.pack()

root.mainloop()