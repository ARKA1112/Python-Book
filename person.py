class Person:
    def __init__(self,name,job=None,pay=0):                        #in operator overloading terms self is the newly created instance object
        self.name = name                                    #name job and pay become state information
        self.job = job                                      #They are local variable within __init__ and when we do self.job it assigns an attribute named job referenced to the local variable name job although they name same but they are two different variables
        self.pay = pay


