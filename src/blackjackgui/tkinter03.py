from tkinter import *

root = Tk()
root.title("My First Frame")
root.geometry("640x480")
root.iconbitmap("src/images/blackjack.ico")

Label(root, text="Welcome to Tkinter.", fg='#630A4A', font=('Curlz MT', 50)).pack()



root.mainloop()