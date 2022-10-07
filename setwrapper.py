class Set:
    def __init__(self, value = []):     #Constructor
        self.data = []                  #Manages a list
        self.concat(value)              #delegation

    def intersect(self, other):         #other is any sequence
        res = []
        for x in self.data:
            if x in other:              #picks common items
                res.append(x)
        return Set(res)                 #Returns new set

    def union(self, other):             #other is any sequence
        res = self.data[:]          #copy of the main list
        for x in other:             #Add other items
            if not x in res:
                res.append(x)
        return Set(res)

    def concat(self, value):            #value is sequence object
        for x in value:
            if not x in self.data:      #Removes duplicates
                self.data.append(x)


    def __len__(self): return len(self.data)                #len(self)
    def __getitem__(self, key): return self.data[key]       #self[i]
    def __and__(self, other): return self.intersect(other)  #self & ot
    def __or__(self, other): return self.union(other) #self|other
    def __repr__(self): return 'Set: ' + repr(self.data) #print()



if __name__ == '__main__':
    x = Set([1,3,5,7])
    print(x.union(Set([1, 4, 7])))
    print(x | Set([1, 4, 6]))
    