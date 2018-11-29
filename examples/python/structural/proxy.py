# Using the proxy pattern, a class represents the functionality of another class.

class Door:
    def __init__(self):
        pass
    
    def open_(self):
        pass
    
    def close(self):
        pass

class LabDoor(Door):
    
    def __init__(self):
        pass
    
    def open_(self):
        return "Opening lab door"
    
    def close(self):
        return "Closing the lab door"


class SecuredDoor:
    
    def __init__(self, door):
        self.door = door
        
    def open_(self, password):
        if self.authenticate(password):
            return self.door.open_()
        else:
            return "Big no! It ain't possible"
    
    def authenticate(self, password):
        return password == "$ecr@t"
    
    def close(self):
       return self.door.close()
    
    
door = SecuredDoor(LabDoor())
print(door.open_("invalid"))
print(door.open_("$ecr@t"))
print(door.close())