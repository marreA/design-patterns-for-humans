
# Facade pattern provides a simplified interface to a complex subsystem.

# A facade is an object that provides a simplified interface to a larger body of code, such as a class library.

class Computer:
    
    def __init__(self):
        pass
    
    def get_electric_shock(self):
        return "Ouch!"
        
    def make_sound(self):
        return "Beep beep!"
    
    def show_loading_screen(self):
        return "Loading..."
    
    def bam(self):
        return "Ready to be used!"
    
    def close_everything(self):
        return "Bup bup bup buzzzzzz!"
    
    def sooth(self):
        return "Zzzzz"
    
    def pull_current(self):
        return "Haaah!"
        

class ComputerFacade:
    
    def __init__(self, computer):
        self.computer = computer
    
    def turn_on(self):
        return " ".join((self.computer.get_electric_shock(), self.computer.make_sound(), self.computer.show_loading_screen(), self.computer.bam()))

    def turn_off(self):
        return " ".join((self.computer.close_everything(), self.computer.pull_current(), self.computer.sooth()))
        

computer = ComputerFacade(Computer())
print(f"\nTurning on the computer\n {computer.turn_on()}")
print(f"Turning off the computer\n {computer.turn_off()}")