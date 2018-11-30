
# Template method defines the skeleton of how a certain algorithm could be performed, but defers the implementation of those steps to the children classes.


class Builder:
    def build(self):
        self.test()
        self.lint()
        self.assemble()
        self.deploy()
        
    def test(self):
        pass
    def lint(self):
        pass
    def assemble(self):
        pass
    def deploy(self):
        pass

class AndroidBuilder(Builder):
    def test(self):
        print("Running android tests")
    
    def lint(self):
        print("Linting the android code")
    
    def assemble(self):
        print("Assembling the android build")
    
    def deploy(self):
        print("Deploying android build to server")

class IosBuilder(Builder):
    def test(self):
        print("Running ios tests")
    
    def lint(self):
        print("Linting the ios code")
        
    def assemble(self):
        print("Assembling the ios build")
    
    def deploy(self):
        print("Deploying ios build to server")


android_builder = AndroidBuilder()
android_builder.build()

ios_builder = IosBuilder()
ios_builder.build()