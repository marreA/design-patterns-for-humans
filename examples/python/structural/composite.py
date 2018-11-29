
# Composite pattern lets clients treat the individual objects in a uniform manner.

class Employee:
    
    def __init__(self, name, salary, roles):
        self.name = name
        self.salary = salary
        self.roles = roles
    

class Developer(Employee):
    
    def __init__(self, name, salary, roles):
        Employee.__init__(self, name, salary, roles)


class Designer(Employee):
    
    def __init__(self, name, salary, roles):
        Employee.__init__(self, name, salary, roles)
        

class Organization:
    
    def __init__(self):
        self.employees = list()
    
    def add_employee(self, employee):
        self.employees.append(employee)

    def get_net_salaries(self):
        net_salary = 0
        for employee in self.employees:
            net_salary += employee.salary
        return net_salary


john = Developer("John Doe", 12000, None)
jane = Designer("Jane Doe", 15000, None)
organization = Organization()
organization.add_employee(john)
organization.add_employee(jane)

print(f"Net salaries: {organization.get_net_salaries()}")
    
