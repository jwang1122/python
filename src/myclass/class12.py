"""
Different object can have differente attribute value.
"""
class Dog:
    def __init__(self, name):
        self.name = name
        self.tricks = []

    def add_trick(self, trick):
        self.tricks.append(trick)


if __name__ == "__main__":
    fido = Dog("Fido")
    buddy = Dog("Buddy")
    fido.add_trick("rool over")
    buddy.add_trick("play dead")
    fido.add_trick("bark")
    buddy.add_trick("bark")
    print(f"what fido can do: {fido.tricks}")
    print(f"what buddy can do: {buddy.tricks}")