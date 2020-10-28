"""define a function inside the class"""
class Robot:
    def say_hi(self):
        print("Hi, I am ", self.name)
    
if __name__ == '__main__':
    x = Robot()
    x.name = "John"
    x.say_hi()