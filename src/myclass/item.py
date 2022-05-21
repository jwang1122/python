class Item:
    discount = 20 # class level attribute

    def __init__(self, name, price, quantity=1) -> None:
        self.name, self.price, self.quantity = name, price, quantity

    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"

    def getTotal(self):
        return self.price * self.quantity

    def addDiscount(self):
        # self.price = self.price * (1-Item.discount/100)
        self.price = self.price * (1-self.discount/100)

if __name__ == '__main__':
    item1 = Item('iPhone', 1000, 2)
    item2 = Item('laptop', 2000)
    print(item1)
    print(f'Total price for {item1.name} is {item1.getTotal()}.')
    print(f'Total price for {item2.name} is {item2.getTotal()}.')
    item1.addDiscount()
    item2.discount = 50
    item2.addDiscount()
    print(f'Total price for {item1.name} is {item1.getTotal():.2f}.')
    print(f'Total price for {item2.name} is {item2.getTotal():.2f}.')

    