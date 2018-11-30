
# It lets you change the behavior of a class when the state changes.

class WrittingState:
    def write(self, words):
        pass
    
class UpperCase(WrittingState):
    def write(self, words):
        return words.upper()
        
class LowerCase(WrittingState):
    def write(self, words):
        return words.lower()

class DefaultText(WrittingState):
    def write(self, words):
        return words
        
class TextEditor:
    _state = None
    def __init__(self, state):
        self._state = state
    
    def set_sate(self, state):
        self._state = state
    
    def type(self, words):
        print(self._state.write(words))


editor = TextEditor(DefaultText())
editor.type("First line")

editor.set_sate(UpperCase())
editor.type("Second line")
editor.type("Third line")

editor.set_sate(LowerCase())
editor.type("Fourth line")
editor.type("Fifth line")