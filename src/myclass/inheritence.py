"""
1. Code reusability
2. Polymorphism
3. default action
4. function overridden
"""
class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print("I don't know what to say...")

class Cat(Pet):
    def __init__(self, /, name, age, color):
        self.color = color
        super().__init__(name, age)

    def speak(self):
        print("Mew...")

class Dog(Pet):
    def speak(self):
        print('Bark...')

class Fish(Pet):
    pass

if __name__ == '__main__':
    c = Cat("bill", 2, 'Black')
    d = Dog("Anglous", 3)
    f = Fish("Jim", 1)
    
    c.speak()
    d.speak()
    f.speak()
