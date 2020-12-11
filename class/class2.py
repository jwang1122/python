"""define a function inside the class"""
class Robot:
    i = 12345
    def say_hi(self):
        print("Hi, I am ", self.name)
    
if __name__ == '__main__':
    x = Robot()
    x.name = "John" # assign attribute name to Robot object
    x.say_hi()
    print(Robot.i)