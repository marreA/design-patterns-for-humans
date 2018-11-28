
# Adapter pattern lets you wrap an otherwise incompatible object in an adapter to make it compatible with another class.

# In software engineering, the adapter pattern is a software design pattern that allows the interface of an existing class to be used as another interface. It is often used to make existing classes work with others without modifying their source code.

# When to use:
#   

class Lion:
    def __init__(self):
        pass
    
    def roar(self):
        return "ROAAAAAAAAAR"

class AfricanLion(Lion):
    def __init__(self):
        pass
    
class AsianLion(Lion):
    def __init__(self):
        pass
    
class Hunter:
    def __init__(self):
        pass
    
    def hunt(self, lion):
        return lion.roar()
        
class WildDog:
    def __init__(self):
        pass
    
    def bark(self):
        return "BARKING"
    
class WildDogAdapter(Lion):
    
    def __init__(self, dog):
        self.dog = dog
        
    def roar(self):
        return self.dog.bark()
        


wild_dog = WildDog()
wild_dog_adapter = WildDogAdapter(wild_dog)

hunter = Hunter()
print(hunter.hunt(wild_dog_adapter))

