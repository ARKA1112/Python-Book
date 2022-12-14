"Assorted class utilities and tools"

class AttrDisplay:
    """
    Provide an inheritable print overload method that displays instances with their class names and a name=value pair for each attribute stored on the instance itself (but not attrs inherited from its classe). Can be mixed into any class, and will work on any instance."""

    def gatherAttrs(self):
        attrs = []
        for key in sorted(self.__dict__):
            attrs.append('%s=%s' % (key,getattr(self,key)))
        return ','.join(attrs)
    def __str__(self):
        return '[%s: %s]' % (self.__class__.__name__, self.gatherAttrs())

if __name__ == '__main__':
    class TopTest(AttrDisplay):    #inherits AttrDisplay
        count = 0
        def __init__(self):
            self.attr1 = TopTest.count
            self.attr2 = TopTest.count + 1
            TopTest.count += 2
        def gatherAttrs(self):
            return 'Spam'

    class SubTest(TopTest):
        pass

    X, Y = TopTest(), SubTest()
    print(X)
    print(Y)