# It helps building a chain of objects. Request enters from one end and keeps going from object to object till it finds the suitable handler.

import abc

class Account(object):
    __metaclass__ = abc.ABCMeta

    _sucessor = None
    _balance = None
    
    def set_next(self, account):
        self._successor = account
    
    def pay(self, amount):
        if (self.can_pay(amount)):
            return f"Paid {amount} using {type(self).__name__}!"
        elif self._successor is not None :
           print(f"Cannot pay using {type(self).__name__}. Proceeding...")
           return self._successor.pay(amount)
        else:
            raise Exception("None of the accounts have enough balance")
    
    def can_pay(self, amout):
        return self._balance >= amout
        

class Bank(Account):
    
    def __init__(self, balance):
        self._balance = balance
        
    
class Paypal(Account):
    
    def __init__(self, balance):
        self._balance = balance
    
class Bitcoin(Account):
    
    def __init__(self, balance):
        self._balance = balance


bank = Bank(100)
paypal = Paypal(200)
bitcoin = Bitcoin(300)

bank.set_next(paypal)
paypal.set_next(bitcoin)

print(bank.pay(259))