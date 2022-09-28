class Person:
    def __init__(self,name,job=None,pay=0):                        #in operator overloading terms self is the newly created instance object
        self.name = name                                    #name job and pay become state information
        self.job = job                                      #They are local variable within __init__ and when we do self.job it assigns an attribute named job                                                  referenced to the local variable name job although they name same but they are two different variables
        self.pay = pay
    def giveRaise(self,percent):
        self.pay = self.pay*(1+ percent/100)
        return self.pay
    def __str__(self):
        return '(Person: %s %s %.2f)' % (self.name, self.job, self.pay)



class Manager(Person):
    def __init__(self, name, pay):
        Person.__init__(self,name, 'mgr' , pay)
    def giveRaise(self, percent, bonus = 10):
        Person.giveRaise(self, percent+bonus)
    def __str__(self):
        return '(Manager: %s %s %.2f %s)' %(self.name, self.job,self.pay,self.hobby)
    def hobby(self,hobby):
        self.hobby = hobby
        print(self.hobby)

if __name__ == '__main__':
    bob = Person('Bob Smith','any',10000)
    sue = Person('Sue Jones', job='dev', pay=10000)
    print(bob.name, bob.pay)
    print(sue.name,sue.job,sue.pay)
    print(bob.name.split()[-1])    #extracts last name
    sue.pay *= 1.10
    print('%.2f'%(sue.pay))
    print(sue)
    tom = Manager('Tom Jones',10000)
    tom.giveRaise(10)
    print('--all three--')
    for object in (bob,sue,tom):       #process objects generically
        object.giveRaise(10)           #Run this object's giveRaise
        print(object)