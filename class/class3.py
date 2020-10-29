"""
__init__(self) function ==> Constructor, or object Factory
Define both attribute and function inside the class

public attribute self.name
"""
class Robot:
    def __init__(self, name):
        self.name = name
        print("__init__() has been called.")

    def say_hi(self):
        print(f"Hi, I am {self.name}.")
    

x = Robot("John Wang")
x.say_hi()
print(x.name)   # Directly access the attribute
