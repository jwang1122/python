"""
class internal function call another internal function
"""
class Bag:
    def __init__(self):
        self.data = []

    def add(self, x):
        self.data.append(x)

    def addtwice(self, x):
        self.add(x)
        self.add(x)

x = Bag()
x.addtwice("apple")
print(x.data)