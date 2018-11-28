
# Factory simply generates an instance for client without exposing any instantiation logic to the client

class Door:
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def __repr__(self):
        pass

class WoodenDoor(Door):
    pass
    def __repr__(self):
        return("WoodenDoor {}x{}".format(self.width, self.height))

class DoorFactory:

    @staticmethod
    def makeDoor(width, height):
        return WoodenDoor(width, height)


door = DoorFactory.makeDoor(100, 200)
door2 = DoorFactory.makeDoor(50, 100)
print(door)
print(door2)