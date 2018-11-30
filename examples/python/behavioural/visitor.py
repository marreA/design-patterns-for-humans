
# Visitor pattern lets you add further operations to objects without having to modify them.

class Animal:
    def accept(self, operation):
        pass
    
    
class AnimalOperation:
    def visit_monkey(self, monkey):
        pass
    
    def visit_lion(self, lion):
        pass
    
    def visit_dolphin(self, dolphin):
        pass

class Monkey(Animal):
    def shout(self):
        print("Ooh oo aa aa!")
        
    def accept(self, operation):
        operation.visit_monkey(self)

class Lion(Animal):
    def roar(self):
        print("Roaaar!")
        
    def accept(self, operation):
        operation.visit_lion(self)

class Dolphin(Animal):
    def speak(self):
        print("Tuut tuttu tuutt!")
    
    def accept(self, operation):
        operation.visit_dolphin(self)

class Speak(AnimalOperation):
    def visit_monkey(self, monkey):
        monkey.shout()
    
    def visit_lion(self, lion):
        lion.roar()
    
    def visit_dolphin(self, dolphin):
        dolphin.speak()


class Jump(AnimalOperation):
    def visit_monkey(self, monkey):
        print("Jumped 20 feet high! on to the tree")
    
    def visit_lion(self, lion):
        print("Jumped 7 feet! Back on the ground!")

    def visit_dolphin(self, dolphin):
        print("Walked on water a little and disappeared")
        

monkey = Monkey()
lion = Lion()
dolphin = Dolphin()

speak = Speak()
jump = Jump()

monkey.accept(speak)
monkey.accept(jump)

lion.accept(speak)
lion.accept(jump)

dolphin.accept(speak)
dolphin.accept(jump)
