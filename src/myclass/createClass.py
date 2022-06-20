def Robot2_init(self, name):
    self.name = name

Robot2 = type("Robot2", 
              (), 
              {"counter":0, 
               "__init__": Robot2_init,
               "sayHello": lambda self: "Hi, I am " + self.name})

x = Robot2("Marvin")
print(x.name)
print(x.sayHello())