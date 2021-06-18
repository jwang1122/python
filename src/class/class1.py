"""Define a function outside of a class"""

def hi(obj):
    print("Hi, I am " + obj.name + "!")

class Robot:
    pass
    
if __name__ ==  '__main__':
    x = Robot()
    x.name = "John"
    hi(x)