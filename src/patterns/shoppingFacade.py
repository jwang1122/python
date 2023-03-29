class Car:
    def __init__(self, gas_level=0):
        self.gas_level = gas_level
    
    def check_gas(self):
        if self.gas_level < 10:
            print("Gas level is low, going to gas station")
            self.go_to_gas_station()
    
    def go_to_gas_station(self):
        print("Arrived at gas station, refueling")
        self.gas_level += 50
    
    def drive(self):
        print("Driving to supermarket")
    
    def drive_home(self):
        print("Driving home")

class ShoppingList:
    def __init__(self, items):
        self.items = items
    
    def get_items(self):
        return self.items

class Supermarket:
    def __init__(self, items_in_stock):
        self.items_in_stock = items_in_stock
    
    def collect_items(self, shopping_list):
        items_to_collect = shopping_list.get_items()
        collected_items = []
        for item in items_to_collect:
            if item in self.items_in_stock:
                print(f"Collected {item}")
                collected_items.append(item)
            else:
                print(f"{item} is out of stock, skipping")
        return collected_items
    
    def check_out(self, items):
        total_cost = 0
        for item in items:
            total_cost += self.items_in_stock[item]
        print(f"Total cost is {total_cost}")

class ShoppingFacade:
    def __init__(self, shopping_list, car, supermarket):
        self.shopping_list = shopping_list
        self.car = car
        self.supermarket = supermarket
    
    def do_shopping(self):
        self.car.check_gas()
        self.car.drive()
        items_collected = self.supermarket.collect_items(self.shopping_list)
        self.supermarket.check_out(items_collected)
        self.car.drive_home()

# Create a shopping list
items_to_buy = ["apple", "banana", "orange", "bread", "milk"]
shopping_list = ShoppingList(items_to_buy)

# Create a car with enough gas
car = Car(gas_level=9)

# Create a supermarket with some items in stock and their prices
items_in_stock = {"apple": 1.0, "banana": 1.5, "orange": 0.5, "bread": 2.0, "milk": 3.0}
supermarket = Supermarket(items_in_stock)

# Create a shopping facade with the shopping list, car, and supermarket
shopping_facade = ShoppingFacade(shopping_list, car, supermarket)

# Do the shopping
shopping_facade.do_shopping()
