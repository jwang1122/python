class Book:
    def __init__(self, title, price):
        self.title = title
        self.price = price
    
    def __str__(self):
        return f"Title: '{self.title}' (Price: ${self.price})"

if __name__ == '__main__':
    book1 = Book("Introduction of Python", 10.99)
    print(book1)