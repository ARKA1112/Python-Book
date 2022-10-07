class Set(list):
    """Here we are creating sets using the properties of list class and its functions"""
    def __init__(self, value = []):        #constructor
        list.__init__([])                  #customizes list
        self.concat(value)                 #Copies mutable defaults


    def intersect(self, other):
        res = []
        for x in self:
            if x in other:
                res.append(x)
        return Set(res)

    def union(self, other):
        res = Set(self)
        res.concat(other)
        return res

    def concat(self, other):
        for x in other:
            if not x in self:
                self.append(x)


    def __and__(self, other): return self.intersect(other)
    def __or__(self, other): return self.union(other)
    def __repr__(self): return 'Set: ' + list.__repr__(self)


if __name__ == '__main__':
    x = Set([1,3,5,6])
    y = Set([2,1,4,5,6])
    print(x, y, len(x))
    print(x.intersect(y), y.union(x))
    print(x & y, x | y)
    x.reverse(); print(x)
    print(type(x))
    print(type(Set))