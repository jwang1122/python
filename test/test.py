class Test:
    def __init__(self):
        self.win = 0

    def win(self):
        self.win += 1
    
if __name__ == '__main__':
    t = Test()
    t.win()
    t.win()
    print(t.win)
