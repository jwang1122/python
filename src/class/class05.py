"""
Define constructor with keyword argument.
"""
class Robot:
    def __init__(self, name=None):
        self.name = name
        print("__init__() has been called.")

    def say_hi(self):
        if self.name:
            print(f"Hi, I am {self.name}.")
        else:
            print("Hi, I am a robot without name yet.")

if __name__ == '__main__':
    x = Robot("John Wang")
    x.say_hi()

    x = Robot()
    x.say_hi()
