class IOString():
    def get_String(self):
        self.str1 = input("Please enter a string: ")
        self.print_String()

    def print_String(self):
        print(self.str1.upper())

IOString().get_String()
