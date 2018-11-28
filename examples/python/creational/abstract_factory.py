
# A factory of factories; a factory that groups the individual but related/dependent factories together without specifying their concrete classes.
# The abstract factory pattern provides a way to encapsulate a group of individual factories that have a common theme without specifying their concrete classes

# When to use: 
#   When there are interrelated dependencies with not-that-simple creation logic involved


class Door:
    
    def get_description(self):
        pass


class WoodenDoor(Door):
    
    def get_description(self):
        return "I am a wooden door"

class IronDoor(Door):
    
    def get_description(self):
        return "I am a iron door"

class DoorFittingExpert:
    
    def get_description(self):
        pass

class Welder(DoorFittingExpert):

    def get_description(self):
        return "I can only fit iron doors"


class Carpenter(DoorFittingExpert):
    
    def get_description(self):
        return "I can only fit wooden doors"
        

class DoorFactory:
    
    def make_door(self):
        pass
    
    def make_fitting_expert(self):
        pass
    
class WoodenDoorFactory(DoorFactory):
    
    def make_door(self):
        return WoodenDoor()
    
    def make_fitting_expert(self):
        return Carpenter()
        
        
class IronDoorFactory(DoorFactory):
    
    def make_door(self):
        return IronDoor()
    
    def make_fitting_expert(self):
        return Welder()
        
        

wooden_factory = WoodenDoorFactory()
door = wooden_factory.make_door()
expert = wooden_factory.make_fitting_expert()
print(door.get_description())
print(expert.get_description())

iron_factory = IronDoorFactory()
iron_door = iron_factory.make_door()
welder = iron_factory.make_fitting_expert()
print(iron_door.get_description())
print(expert.get_description())