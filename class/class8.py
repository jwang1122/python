from enum import Enum
"""
class Inheritance
Class level function
Class level attribute
"""

class Mood(Enum): # Mood class inherites from Enum class
    FUNKY = 1
    HAPPY = 3

    def describe(self):
        return self.name, self.value

    @classmethod
    def favorite_mood(cls):
        return cls.HAPPY

if __name__ == '__main__':
    print(Mood.favorite_mood()) # use class name call function
    print(Mood.FUNKY.value) # use class name access attribute