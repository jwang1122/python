# Define the base component
class Pizza:
    def __init__(self):
        self.description = "Unknown Pizza"
    
    def get_description(self):
        return self.description
    
    def get_cost(self):
        pass

# Define concrete components
class MargheritaPizza(Pizza):
    def __init__(self):
        self.description = "Margherita Pizza"
        
    def get_cost(self):
        return 10.0

class PepperoniPizza(Pizza):
    def __init__(self):
        self.description = "Pepperoni Pizza"
        
    def get_cost(self):
        return 12.0

# Define the decorator class
class PizzaDecorator(Pizza):
    def __init__(self, pizza):
        self.pizza = pizza
    
    def get_description(self):
        return f"{self.pizza.get_description()}, {self.description}"
    
    def get_cost(self):
        return self.pizza.get_cost()

# Define concrete decorators
class ExtraCheese(PizzaDecorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.description = "Extra Cheese"
    
    def get_cost(self):
        return self.pizza.get_cost() + 1.0

class Mushrooms(PizzaDecorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.description = "Mushrooms"
    
    def get_cost(self):
        return self.pizza.get_cost() + 0.5

# Create a Margherita pizza with extra cheese and mushrooms
pizza = MargheritaPizza()
pizza = ExtraCheese(pizza)
pizza = Mushrooms(pizza)

# Print the description and cost
print(pizza.get_description())
print(pizza.get_cost())
