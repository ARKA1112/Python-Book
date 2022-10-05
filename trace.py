class wrapper:
    def __init__(self, object):
        self.wrapped = object
    def __getattr__(self, name):
        print('Trace :', name)
        return getattr(self.wrapped, name)