from tkinterbase import *

class MainFrame(BaseWindow):
    def buildWidgets(self):
        self.root.configure(bg='#00FFFF')
        self.boardFrame = PlayBoardFrame(self)
        self.configFrame = ConfigFrame(self)
        self.configFrame.pack(fill=BOTH, expand=1)
    
    def switchToBoardFrame(self):
        self.configFrame.hide()
        self.boardFrame.pack(fill=BOTH, expand=1)

    def switchToConfigFrame(self):
        self.boardFrame.hide()
        self.configFrame.pack(fill=BOTH, expand=1)

class ConfigFrame():
    def __init__(self, parent):
        self.parent = parent
        self.frame = Frame(parent.root, bg='#FFFF00')
        Label(self.frame, text="I am the Configure Frame...").pack()
        Button(self.frame, text="to Board Frame", command=self.switch).pack()

    def pack(self, **kwargs):
        self.frame.pack(kwargs)

    def hide(self):
        self.frame.pack_forget() # this built in function get ride of this frame

    def switch(self):
        self.parent.switchToBoardFrame()

class PlayBoardFrame():
    def __init__(self, parent):
        self.parent = parent
        self.frame = Frame(parent.root, bg='#90F3C5')
        Label(self.frame, text="I am the Play Board Frame...").pack()
        Button(self.frame, text="to Config Frame", command=self.switch).pack()

    def pack(self, **kwargs):
        self.frame.pack(kwargs)

    def hide(self):
        self.frame.pack_forget() # this built in function get ride of this frame

    def switch(self):
        self.parent.switchToConfigFrame()


if __name__ == '__main__':
    MainFrame()