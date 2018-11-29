
# Allows you to create different flavors of an object while avoiding constructor pollution. Useful when there could be several flavors of an object. Or when there are a lot of steps involved in creation of an object.

# The builder pattern is an object creation software design pattern with the intentions of finding a solution to the telescoping constructor anti-pattern.

# When to use: 
#   When there could be several flavors of an object and to avoid the constructor telescoping. The key difference from the factory pattern is that; factory pattern is to be used when the creation is a one step process while builder pattern is to be used when the creation is a multi step process.

class Burger:
    
    def __init__(self, burger_builder):
        self.size = burger_builder.size
        self.cheese = burger_builder.cheese
        self.pepperoni = burger_builder.pepperoni
        self.lettuce = burger_builder.lettuce
        self.tomato = burger_builder.tomato

    def __repr__(self):
        return f"Burger: size={self.size}, cheese={self.cheese}," \ 
        f"pepperoni={self.pepperoni}, lettuce={self.lettuce}, tomato={self.tomato}"

class BurgerBuilder:
    
    def __init__(self, size, pepperoni = False, lettuce = False, cheese = False, tomato = False):
        self.size = size
        self.pepperoni = pepperoni
        self.lettuce = lettuce
        self.cheese = cheese
        self.tomato = tomato
    
    def build(self):
        return Burger(self)
        

burger = BurgerBuilder(14, True, True, True, True).build()
print(burger)