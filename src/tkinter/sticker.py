from tkinter import *
from tkinterbase import *
from tkinter import filedialog as fd

class Sticker(TkinterBase):
    def buildWidget(self):
        self.root.protocol("WM_DELETE_WINDOW", self.callback)

        self.text = Text(self.root)
        self.text.grid(row=0, column=0, columnspan=5)
        
        Button(self.root, text="Open", command=self.open).grid(row=1,column=1)
        Button(self.root, text="Save", command=self.save).grid(row=1,column=2)
        Button(self.root, text="clear", command=self.clear).grid(row=1,column=3)
        self.openDefault()
    
    def callback(self):
        self.saveDefault()
        self.root.destroy()

    def clear(self):
        self.text.delete('1.0', END)

    def save(self):
        files = [('All Files', '*.*'), 
             ('Python Files', '*.py'),
             ('Text Document', '*.txt')]
        self.file = fd.asksaveasfile(mode='w', filetypes=files, defaultextension=".py")
        self.file.write(self.text.get(1.0, END))
        self.file.close()

    def openDefault(self):
        with open("sticker.txt") as f:
            contents = f.read()
        self.text.insert(INSERT, contents)

    def saveDefault(self):
        with open("sticker.txt", "+w") as f:
            f.write(self.text.get(1.0, END))
    
    def open(self):
        self.filename = fd.askopenfilename()
        with open(self.filename) as f:
            contents = f.read()
        self.text.insert(INSERT, contents)

if __name__ == '__main__':
    Sticker()