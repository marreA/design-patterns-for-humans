# Allows you to encapsulate actions in objects. The key idea behind this pattern is to provide the means to decouple client from receiver.


class Bulb:
    def turn_on(self):
         print("Bulb has been lit")
        
    def turn_off(self):
        print("Darkness!")


class Command:
    
    def execute(self):
        pass

    def undo(self):
        pass
    
    def redo(self):
        pass
    

class TurOn(Command):
    
    def __init__(self, bulb):
        self.bulb = bulb
    
    def execute(self):
        self.bulb.turn_on()
    
    def undo(self):
        self.bulb.turn_off()
    
    def redor(self):
        self.execute()


class TurnOff(Command):
    
    def __init__(self, bulb):
        self.bulb = bulb
    
    
    def execute(self):
        self.bulb.turn_off()
    
    def undo(self):
        self.bulb.turn_on()
    
    def redo(self):
        self.execute()


class RemoteControl:
    
    def submit(self, command):
        command.execute()


bulb = Bulb()
turn_on = TurOn(bulb)
turn_off = TurnOff(bulb)
remote = RemoteControl()

remote.submit(turn_on)
remote.submit(turn_off)