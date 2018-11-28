
# Ensures that only one object of a particular class is ever created.

# In software engineering, the singleton pattern is a software design pattern that restricts the instantiation of a class to one object. This is useful when exactly one object is needed to coordinate actions across the system.

# When to use:
# 


class President:
    
    __instance = None
    def __init__(self):
        if President.__instance != None:
            raise Exception("This class is a singleton")
        else:
            President.__instance = self

    def __str__(self):
        return repr(self)
    
    @staticmethod
    def get_instance():
        if President.__instance == None:
            President()
        return President.__instance

president = President.get_instance()
president2 = President.get_instance()
print(president)
print(president2)

print(president == president2)