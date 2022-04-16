"""
titled frame
"""

from tkinter import *
screen = Tk()
screen.geometry("400x200")
win4 = StringVar()
win4.set("0")
labelframe = LabelFrame(screen, text = "Game Result", bg=('#FFFF00'))
Label(labelframe, text="John", bg=('#FFFF00')).grid(row=0, column=0)
Label(labelframe, text="0", bg=('#FFFF00')).grid(row=0, column=1)
Label(labelframe, text="Julianne", bg=('#FFFF00')).grid(row=1, column=0)
Label(labelframe, text="0", bg=('#FFFF00')).grid(row=1, column=1)
Label(labelframe, text="Daniel", bg=('#FFFF00')).grid(row=2, column=0)
Label(labelframe, text="0", bg=('#FFFF00')).grid(row=2, column=1)
Label(labelframe, text="Wyatt", bg=('#FFFF00')).grid(row=3, column=0)
win4Lbl = Label(labelframe, textvariable=win4, bg=('#FFFF00'))
win4Lbl.grid(row=3, column=1)
labelframe.place(x=200, y=10, width=150, height=120)

win4.set("4")

screen.mainloop()