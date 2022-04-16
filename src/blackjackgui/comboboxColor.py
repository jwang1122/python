from tkinter import*
from tkinter.ttk import Combobox
from turtle import width

screen = Tk()
screen.geometry("255x150")
screen.title("Set Player's seat")
screen.configure(bg='yellow')
myText = StringVar()
myText.set('blue')
Label(screen, text="Available Seats:",bg='yellow').grid(row=1, column=0)
colorDict = {'blue':'#0000FF', 'yellow':'#FFEE50', 'cyan':'#00FFFF', 'red':'#EE0088'}
combobox = Combobox(screen,textvariable=myText,values=list(colorDict.keys()))
combobox.grid(row=1, column=1)
setBtn = Button(screen, text="Set", width=20)
setBtn.place(x=55, y=120)

def change(event):
    text = myText.get()
    print(colorDict[text])

combobox.bind("<<ComboboxSelected>>", func=change)
screen.mainloop()