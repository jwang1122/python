from typing import List

class Observer:
    def update(self):
        pass

class Subject:
    def __init__(self):
        self.observers: List[Observer] = []

    def add_observer(self, observer: Observer):
        self.observers.append(observer)

    def remove_observer(self, observer: Observer):
        self.observers.remove(observer)

    def notify_observers(self):
        for observer in self.observers:
            observer.update()

class ShoppingList:
    def __init__(self, items):
        self.items = items
        self.is_completed = False

    def mark_completed(self):
        self.is_completed = True

class GasChecker(Observer):
    def __init__(self, shopping_process):
        self.shopping_process = shopping_process

    def update(self):
        if self.shopping_process.gas_level < 5:
            print("Gas level is low. Need to go to gas station.")
            self.shopping_process.go_to_gas_station()

class GasStation:
    def refill_gas(self):
        print("Refilling gas...")

class Supermarket(Observer):
    def __init__(self, shopping_process):
        self.shopping_process = shopping_process

    def update(self):
        print("Going to supermarket to buy items...")
        self.shopping_process.buy_items()

class Checkout(Observer):
    def update(self):
        print("Checking out items...")
        print("Items checked out.")

class ShoppingProcess(Subject):
    def __init__(self, items):
        super().__init__()
        self.shopping_list = ShoppingList(items)
        self.gas_level = 10
        self.is_at_gas_station = False
        self.is_at_supermarket = False

    def add_observer(self, observer: Observer):
        super().add_observer(observer)
        observer.shopping_process = self

    def go_to_gas_station(self):
        self.is_at_gas_station = True
        self.is_at_supermarket = False
        self.gas_station = GasStation()
        self.gas_station.refill_gas()
        self.gas_level = 10
        self.is_at_gas_station = False
        self.notify_observers()

    def go_to_supermarket(self):
        self.is_at_supermarket = True
        self.is_at_gas_station = False
        self.supermarket = Supermarket(self)
        self.supermarket.update()

    def buy_items(self):
        print("Buying items from supermarket...")
        self.shopping_list.mark_completed()
        self.checkout = Checkout()
        self.checkout.update()
        self.notify_observers()

    def run(self):
        print("Starting shopping process...")
        gas_checker = GasChecker(self)
        self.add_observer(gas_checker)
        self.go_to_supermarket()

shopping_process = ShoppingProcess(['bread', 'milk', 'eggs'])
shopping_process.run()
