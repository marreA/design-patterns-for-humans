import abc

# It provides a way to delegate the instantiation logic to child classes.

# Useful when there is some generic processing in a class but the required sub-class is dynamically decided at runtime. Or putting it in other words, when the client doesn't know what exact sub-class it might need.

class Interviewer(object):
    
    __metaclass__ = abc.ABCMeta
    def __init__(self):
        pass

    @abc.abstractmethod
    def ask_question(self):
        return
    
class Developer(Interviewer):
    
    def ask_question(self):
        return "Asking about design patterns!"

class CommunityExecutive(Interviewer):
    
    def ask_question(self):
        return 'Asking about community building!'
        

class HiringManager(object):
    __metaclass__ = abc.ABCMeta
    
    def takeInterview(self):
        interviewer = self.make_interviewer()
        return interviewer.ask_question()
        
    @abc.abstractmethod
    def make_interviewer(self):
        return

class DevelopmentManager(HiringManager):
    def make_interviewer(self):
        return Developer()

class MarketingManager(HiringManager):
    def make_interviewer(self):
        return CommunityExecutive()


dev_manager = DevelopmentManager()
print(dev_manager.takeInterview())

marketing_manager = MarketingManager()
print(marketing_manager.takeInterview())