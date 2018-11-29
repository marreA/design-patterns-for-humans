# Bridge pattern is about preferring composition over inheritance. Implementation details are pushed from a hierarchy to another object with a separate hierarchy.

# The bridge pattern is a design pattern used in software engineering that is meant to "decouple an abstraction from its implementation so that the two can vary independently"


class WebPage:
    
    def __init__(self, theme):
        self.theme = theme
    
    def get_content(self):
        pass
    
    
class About(WebPage):
    
    def __init__(self, theme):
        WebPage.__init__(self, theme)
    
    def get_content(self):
        return f"About page in {self.theme.color} theme"
        

class Careers(WebPage):
    
    def __init__(self, theme):
        WebPage.__init__(self, theme)
    
    def get_content(self):
        return f"Careers page in {self.theme.color} theme"


class Theme:
    def __init__(self, color):
        self.color = color
        

class DarkTheme(Theme):
    def __init__(self):
        Theme.__init__(self, "Dark Black")

class LightTheme(Theme):
    def __init__(self):
        Theme.__init__(self, "Off white")


class AquaTheme(Theme):
    def __init__(self):
        Theme.__init__(self, "Ligth Blue")



dark_theme = DarkTheme()
about = About(dark_theme)
careers = Careers(dark_theme)

print(about.get_content())
print(careers.get_content())


