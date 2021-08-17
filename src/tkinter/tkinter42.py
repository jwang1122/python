"""
display image on frame
"""
from tkinter import *
from tkinter import ttk
 
def TestLogic():
    stgImg = PhotoImage(file="images/diamond5.gif")
    label=ttk.Label(root, image=stgImg)
    label.configure(image=stgImg)
    label.image = stgImg
    label.place(x=10, y=20)
 
root = Tk()
 
root.geometry('1010x740+200+200')
  
stgImg1 = PhotoImage(file="images/heartQ.gif")
label1=ttk.Label(root, image=stgImg1)
label1.place(x=400, y=400)
  
testBtn=ttk.Button(root, text="TEST", command=TestLogic)
testBtn.place(x=400, y=200)
root.mainloop()
