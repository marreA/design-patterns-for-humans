# Decorator pattern lets you dynamically change the behavior of an object at run time by wrapping them in an object of a decorator class.


class Coffee:
    def __init__(self, cost, description):
        self.cost = cost
        self.description = description

class SimpleCoffe(Coffee):
    
    def __init__(self):
        Coffee.__init__(self, 10, "Simple Coffee")


class MilkCoffee(Coffee):
    
    def __init__(self, coffee):
        self.coffee = coffee
        self.cost = self.coffee.cost + 2
        self.description = self.coffee.description + ", milk"

class WhipCoffee(Coffee):
    
    def __init__(self, coffee):
        self.coffee = coffee
        self.cost = self.coffee.cost + 5
        self.description = self.coffee.description + ", whip"


class VanillaCoffee(Coffee):
    
    def __init__(self, coffee):
        self.coffee = coffee
        self.cost = self.coffee.cost + 3
        self.description = self.coffee.description + ", vanilla"
        

some_coffee = SimpleCoffe()
print(f"Some coffe cost: {some_coffee.cost}, description: {some_coffee.description}")

some_coffee = MilkCoffee(some_coffee)
print(f"Some coffee cost: {some_coffee.cost}, description: {some_coffee.description}")

some_coffee = WhipCoffee(some_coffee)
print(f"Some coffee cost: {some_coffee.cost}, description: {some_coffee.description}")

some_coffee = VanillaCoffee(some_coffee)
print(f"Some coffee cost: {some_coffee.cost}, description: {some_coffee.description}")






