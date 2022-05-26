import csv

class Store:
    items = []
    def addItem(self, item):
        Store.items.append(item)

    @classmethod
    def getAllItems(cls):
        return cls.items

    @classmethod
    def save(cls, file):

        with open(file, mode='+w') as f:
            f.write('Name,Price,Quantity\n')
            for item in cls.items:
                f.write(f'{item.name},{item.price},{item.quantity}\n')
        print('Save Data Successful')

    @classmethod
    def load(cls, file):
        with open(file, newline='') as f:
            data = csv.DictReader(f)
            for item in list(data):
                Item(item['Name'], item['Price'], item['Quantity'])

        print('Load data Successful')
        
class Item:
    discount = 20 # class level attribute
    store = Store()

    def __init__(self, name, price, quantity=1) -> None:
        self.name, self.price, self.quantity = name, price, quantity
        Item.store.addItem(self)

    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"

    def getTotal(self):
        return self.price * self.quantity

    def addDiscount(self):
        # self.price = self.price * (1-Item.discount/100)
        self.price = self.price * (1-self.discount/100)


if __name__ == '__main__':
    item1 = Item('iPhone', 1000, 2)
    # item2 = Item('laptop', 2000, 10)
    # item3 = Item('mouse', 24, 20)
    # item4 = Item('monitor', 100, 15)
    # item5 = Item('keyboard', 20, 100)
    # item6 = Item('desktop', 400, 13)

    # print(Item.store.items)
    
    # Store.save('items.csv')
    
    Store.load('items.csv')
    print(Store.items)