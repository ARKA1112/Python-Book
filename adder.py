def adder(**kwargs):
    a = kwargs.get(0,0)   #gets the zeroeth position in kwargs dict else returns o
    for k in kwargs.keys():
        a = a + kwargs[k]
    return a



