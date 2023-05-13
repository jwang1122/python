class Animal:
    def __init__(self, name):
        self.name = name
    
    def eat(self):
        print(f"{self.name} is eating.")

class Mammal(Animal):
    def __init__(self, name):
        super().__init__(name)
    
    def walk(self):
        print(f"{self.name} is walking.")

class Bird(Animal):
    def __init__(self, name):
        super().__init__(name)
    
    def fly(self):
        print(f"{self.name} is flying.")

class Bat(Mammal, Bird): # Bat inherits from both Mammal and Bird classes.
    def __init__(self, name):
        super().__init__(name)

bat = Bat("Batty")
bat.eat() # Output: Batty is eating.
bat.walk() # Output: Batty is walking.
bat.fly() # Output: Batty is flying.
