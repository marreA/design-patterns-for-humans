# Create object based on an existing object through cloning.

# The prototype pattern is a creational design pattern in software development. It is used when the type of objects to create is determined by a prototypical instance, which is cloned to produce new objects.

# When to use:
# When an object is required that is similar to existing object or when the creation would be expensive as compared to cloning.



import copy

class Sheep:
    
    def __init__(self, name, category = "Mountain Sheep"):
        self.name = name
        self.category = category
    
    def __repr__(self):
        return f"Hi I am {self.name}, and I am a {self.category}"
        
original = Sheep('Jolly')
print(original)
cloned = copy.copy(original)
cloned.name = "Dolly"
print(cloned)