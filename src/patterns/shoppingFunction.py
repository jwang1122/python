def create_shopping_list(items):
    return items

def check_gas(gas_level):
    if gas_level < 10:
        print("Gas level is low, going to gas station")
        gas_level += 50
    return gas_level

def drive():
    print("Driving to supermarket")

def collect_items(shopping_list, items_in_stock):
    items_to_collect = shopping_list
    collected_items = []
    for item in items_to_collect:
        if item in items_in_stock:
            print(f"Collected {item}")
            collected_items.append(item)
        else:
            print(f"{item} is out of stock, skipping")
    return collected_items

def check_out(items, items_in_stock):
    total_cost = 0
    for item in items:
        total_cost += items_in_stock[item]
    print(f"Total cost is {total_cost}")

def drive_home():
    print("Driving home")

def do_shopping(items_to_buy, gas_level, items_in_stock):
    shopping_list = create_shopping_list(items_to_buy)
    gas_level = check_gas(gas_level)
    drive()
    items_collected = collect_items(shopping_list, items_in_stock)
    check_out(items_collected, items_in_stock)
    drive_home()

# Create a shopping list
items_to_buy = ["apple", "banana", "orange", "bread", "milk"]

# Set initial gas level
gas_level = 3

# Create a dictionary with items in stock and their prices
items_in_stock = {"apple": 1.0, "banana": 1.5, "orange": 0.5, "bread": 2.0, "milk": 3.0}

# Do the shopping
do_shopping(items_to_buy, gas_level, items_in_stock)
