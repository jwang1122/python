class Robot:
    def say_hi(self):
        print("Hi, I am ", self.name)
    

x = Robot()
x.name = "John"
x.say_hi()