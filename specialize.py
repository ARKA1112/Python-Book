class Super:
    def method(self):
        print('in super method')
    def delegate(self):
        self.action()    #expects to be defined

class Inheritor(Super):
    pass          #inherits super

class Replacer(Super):
    def method(self):
        print('in replacer method')

class Extender(Super):
    def method(self):
        print('in extender method')
        Super.method(self)
        print('ending extender method')

class Provider(Super):
    def action(self):
        print('Provider in action')
        print(self.__dict__.keys())

if __name__ == '__main__':
    for klass in (Inheritor, Replacer, Extender, Provider):
        print('\n'+ klass.__name__ + '...')
        klass().method()
    print('\nProvider.....')
    x  = Provider()
    x.delegate()