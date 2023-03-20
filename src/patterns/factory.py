class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

class AnimalFactory:
    def create_animal(self, animal_type, name):
        if animal_type == 'dog':
            return Dog(name)
        elif animal_type == 'cat':
            return Cat(name)
        else:
            return None

# Usage
animal_factory = AnimalFactory()

dog = animal_factory.create_animal('dog', 'Fido')
cat = animal_factory.create_animal('cat', 'Whiskers')

print(dog.speak())
print(cat.speak())
