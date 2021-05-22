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

    mood1 = Mood(1)
    print(f"mood1: {mood1}")
    print(f"mood1.FUNKY: {mood1.FUNKY}")
    print(f"call mood1.favorite_mood(): {mood1.favorite_mood()}")
    print()

    mood2 = Mood(3)
    print(f"mood2: {mood2}")
    print(f"mood2.FUNKY: {mood2.FUNKY}")
    print(f"call mood2.favorite_mood(): {mood2.favorite_mood()}")
    
    mood3 = Mood()