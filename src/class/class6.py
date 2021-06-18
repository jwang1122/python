"""
protected attribute: self._name
private attribute: self.__energy
"""

class Robot:
    def __init__(self, name=None, energy=1000):
        self._name = name       # protected attribute
        self.__energy = energy  # private attribute
        print("__init__() has been called.")

    def say_hi(self):
        if self._name:
            print(f"Hi, I am {self._name}.")
        else:
            print("Hi, I am a robot without name yet.")
        print("I have energy of", self.__energy)
        
if __name__ == '__main__':
    x = Robot("John Wang")
    x.say_hi()

    x = Robot()
    x.say_hi()

    print("25:",x._name)    # Protected attribute
    print("26:",x.__energy) # Private attribute