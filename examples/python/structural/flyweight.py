
# It is used to minimize memory usage or computational expenses by sharing as much as possible with similar objects.

class KarakTea:
    def __init__(self):
        pass
    
    def __repr__(self):
        return "KarakTea"

class TeaMaker:
    def __init__(self):
        self.available_tea = dict()
        
    def make(self, preference):
        if preference not in self.available_tea:
            self.available_tea[preference] = KarakTea()
        return self.available_tea[preference]

class TeaShop:
    
    def __init__(self, tea_maker):
        self.tea_maker = tea_maker
        self.orders = dict()
    
    def take_order(self, tea_type, table):
        self.orders[table] = self.tea_maker.make(tea_type)
    
    def serve(self):
        for key, value in self.orders.items():
            print(f"Serving tea {value} to table{key}")


tea_maker = TeaMaker()
shop = TeaShop(tea_maker)
shop.take_order("less sugar", 1)
shop.take_order("more milk", 2)
shop.take_order("without sugar", 5)

shop.serve()