"""
using tk.Frame
"""
import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.bind('<Enter>', self.turnBlue)
        self.hi_there.pack()

        self.text = tk.Text(self.master)
        self.quit = tk.Button(self, text="QUIT", fg="red", bg='yellow',
                              command=self.master.destroy)
        self.text.pack()
        self.quit.pack()

    def say_hi(self):
        self.text.insert("1.0","hi there, everyone!")

    def turnBlue(self, event):
        event.widget['activeforeground'] = 'white'
        event.widget['activebackground'] = 'blue'

if __name__ == '__main__':   
    root = tk.Tk()
    root.title("My First Window")
    root.geometry('280x150')
    app = Application(master=root)
    app.mainloop()
