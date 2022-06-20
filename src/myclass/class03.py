"""
define a function inside the class
"""
class Robot:
    i = 12345
    def say_hi(self):
        print("Hi, I am ", self.name)
    
    def isInteger(num): # class level function can be called by class name
        if isinstance(num, float):
            return num.is_integer()
        return isinstance(num, int)
        # elif isinstance(num, int):
        #     return True
        # else:
        #     return False

    def add(x, y): 
        return x + y

    def sub(self, x, y): # instance level function
        return x - y

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
    
    print(Robot.add(3, 5))
    print(x.sub(5,6))
    print(Robot.sub(x, 5, 6))
    # print(x.add(3,12)) # TypeError: Robot.add() takes 2 positional arguments but 3 were given

    print(Robot.isInteger(12.0))
    print(Robot.isInteger(23))
    print(Robot.isInteger(3.14159))