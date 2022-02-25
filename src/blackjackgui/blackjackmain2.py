from tkinterbase import *

class MainFrame(BaseWindow):
    def buildWidgets(self):
        self.configFrame = ConfigFrame(self)
        self.boardFrame = BoardFrame(self)
        self.configFrame.pack(fill='both', expand=1)

    def switchToConfigFrame(self):
        self.configFrame.pack(fill='both', expand=1)
        self.boardFrame.pack_forget()

    def switchToBoardFrame(self):
        self.boardFrame.pack(fill='both', expand=1)
        self.configFrame.pack_forget()

class ConfigFrame():
    def __init__(self, parent):
        self.parent = parent
        self.frame = Frame(parent.root)
        self.frame.configure(bg='#568568')
        welcomeLbl = Label(self.frame, text='Welcome to Our Blackjack Game!', bg='#568568', fg='#630A4A', font=('Arial Bold', 30)) #RGB in Hex
        welcomeLbl.pack(pady=30)
        mainImage = PhotoImage(file='src/images/animation.gif')
        imageLbl = Label(self.frame)
        imageLbl.configure(image=mainImage)
        imageLbl.image = mainImage
        imageLbl.pack()
        startBtn = Button(self.frame, text="Start", command=self.switch)
        startBtn.pack(pady=30)

    
    def pack(self, **kwargs):
        self.frame.pack(kwargs)
  
    def pack_forget(self):
        self.frame.pack_forget()

    def switch(self):
        self.parent.switchToBoardFrame()

class BoardFrame():
    def __init__(self, parent):
        self.parent = parent
        self.frame = Frame(parent.root)
        Label(self.frame, text="Play Board Frame").pack()
        Button(self.frame, text="to Config Frame", command=self.switch).pack()

    def pack(self, **kwargs):
        self.frame.pack(kwargs)
  
    def pack_forget(self):
        self.frame.pack_forget()
        
    def switch(self):
        self.parent.switchToConfigFrame()

if __name__ == '__main__':
    MainFrame()
