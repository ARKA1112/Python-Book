class Person:
    def __init__(self,name,job=None,pay=0):                        #in operator overloading terms self is the newly created instance object
        self.name = name                                    #name job and pay become state information
        self.job = job                                      #They are local variable within __init__ and when we do self.job it assigns an attribute named job                                                  referenced to the local variable name job although they name same but they are two different variables
        self.pay = pay
    def giveRaise(self,percent):
        self.pay = self.pay*(1+ percent/100)
        return self.pay




class Manager(Person):
    def giveRaise(self, percent, bonus = 10):
        Person.giveRaise(self, percent+bonus)
    def __str__(self):
        return '(Manager: %s %s %f' %(self.name, self.job,self.pay)


if __name__ == '__main__':
    bob = Person('Bob Smith')
    sue = Person('Sue Jones', job='dev', pay=100000)
    print(bob.name, bob.pay)
    print(sue.name,sue.job,sue.pay)
    print(bob.name.split()[-1])    #extracts last name
    sue.pay *= 1.10
    print('%.2f'%(sue.pay))
    print(sue)
    tom = Manager('Tom Jones','mgr',10000)
    tom.giveRaise(10)