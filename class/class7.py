"""
access none public attributes, getter, setter and property

protected attribute: self._name
private attribute: self.__energy
define property related to accessing functions (name)
"""

class Robot:
    def __init__(self, name=None, energy=1000):
        self._name = name       # protected attribute
        self.__energy = energy  # private attribute
        print("__init__() has been called.")

    def __repr__(self):
        return self._name

    def say_hi(self):
        if self._name:
            print(f"Hi, I am {self._name}.")
        else:
            print("Hi, I am a robot without name yet.")
        print("I have energy of", self.__energy)
        
    def getName(self):
        return self._name

    def getEnerge(self):
        return self.__energy

    def setName(self, name):
        self._name = name

    def delName(self):
        print('delname() called')
        del self._name

    name = property(getName, setName, delName)

if __name__ == '__main__':
    x = Robot("John Wang")
    x.say_hi()

    # x = Robot()
    # x.say_hi()

    print("39:",x._name)    # Protected attribute
    # print("35:",x.__energy) # Private attribute

    print("42:",x.getName())
    print("43:", x.getEnerge())

    print("45:", x.name)
    x.name = "Charles"
    print("47:",x.name)

    # del x.name
    # print(x._name)