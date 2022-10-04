"""Our pizzshop is a composite object, it has an oven and it has employees like servers and chefs. When a customer enters and places an order the components of the shop spirng into action the server takes the order the ched makes the pizza and so on. The following example simultaes all the objects and relationships in this scenario"""

from employees import PizzaBot, Server

class Customer:
    def __init__(self, name):
        self.name = name
    def order(self, server):
        print(self.name, 'orders from', server)
    def pay(self, server):
        print(self.name, 'pays for item to ', server)

class Oven:
    def bake(self):
        print('oven bakes')

class Pizzashop:
    def __init__(self):
        self.server = Server('pat')   #Embed other objects
        self.chef = PizzaBot('Bob')   #A robot named bob
        self.oven = Oven()

    def order(self, name):
        customer = Customer(name)
        customer.order(self.order)
        self.chef.work()
        self.oven.bake()
        customer.pay(self.server)