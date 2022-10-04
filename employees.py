#creating class employee
class Employee:
    def __init__(self, name, salary = 0):
        self.name = name
        self.salary = salary
    def giveraise(self, percent):
        self.salary = self.salary *(1+percent/100)
    def work(self):
        print(self.name, 'does stuff')
    def __repr__(self):
        return "<Employee {}, salary = {}>".format(self.name, self.salary)
#going into the specifics of the employee
#defining chef class
class Chef(Employee):
    def __init__(self,name):
        Employee.__init__(self, name, 50000)
    def work(self):
        print(self.name," works as a chef")

class Server(Employee):
    def __init__(self, name):
        Employee.__init__(self, name, 40000)
    def work(self):
        print(self.name, "interfaces with customer")
        
class PizzaBot(Chef):
    def __init__(self, name):
        super().__init__(name)
        return print(self.name)  #added this return myself
    def work(self):
        print(self.name, " makes pizza")

if __name__ == "__main__":
    bob = PizzaBot('bob')
    print(bob)
    bob.work()
    bob.giveraise(20)
    print(bob); print()

    for klass in Employee, Chef, Server, PizzaBot:
        obj = klass(klass.__name__)
        obj.work()