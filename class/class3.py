class Robot:
    def __init__(self, name):
        self.name = name
        print("__init__() has been called.")

    def say_hi(self):
        print(f"Hi, I am {self.name}.")
    

x = Robot("John Wang")
x.say_hi()