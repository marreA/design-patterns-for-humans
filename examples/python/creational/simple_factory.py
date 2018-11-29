
# Factory simply generates an instance for client without exposing any instantiation logic to the client

# When creating an object is not just a few assignments and involves some logic, it makes sense to put it in a dedicated factory instead of repeating the same code everywhere.


class Door:
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def __repr__(self):
        pass

class WoodenDoor(Door):
    pass
    def __repr__(self):
        return f"WoodenDoor {self.width}x{self.height}"

class DoorFactory:

    @staticmethod
    def makeDoor(width, height):
        return WoodenDoor(width, height)


door = DoorFactory.makeDoor(100, 200)
door2 = DoorFactory.makeDoor(50, 100)
print(door)
print(door2)