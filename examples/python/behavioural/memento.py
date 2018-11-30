
# Memento pattern is about capturing and storing the current state of an object in a manner that it can be restored later on in a smooth manner.

class EditorMemento:
    
    _content = None
    def __init__(self, content):
        self._content = content
        
    def get_content(self):
        return self._content


class Editor:
    
    _content = ""
    
    def __init__(self):
        pass
    
    def type(self, words):
        self._content = f"{self._content} {words}"
    
    def get_content(self):
        return self._content
    
    def save(self):
        return EditorMemento(self._content)
        
    def restore(self, memento):
        self._content = memento.get_content()


editor = Editor()
editor.type("This is the first sentence")
editor.type("This is second")
saved = editor.save()

editor.type("And this is third")
print(editor.get_content())

editor.restore(saved)
print(editor.get_content())