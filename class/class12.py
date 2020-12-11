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
    print(fido.tricks)