"""
define a function inside the class
"""
class Robot:
    i = 12345
    def say_hi(self):
        print("Hi, I am ", self.name)
    
if __name__ == '__main__':
    x = Robot()
    x.name = "John" # assign attribute name to Robot object
#    Robot.say_hi() # TypeError: Robot.say_hi() missing 1 required positional argument: 'self' 
    Robot.say_hi(x)
    # x.say_hi() # robot object can introduce itself
    print(Robot.i)

    a = 5
    print(a.__gt__(3))
    print((1,2).__lt__(7)) # NotImplemented
    print([1,2].__iter__())
    print([1,2,3].__iter__().__next__()) # . operators can be used continuously
    
    