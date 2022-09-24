def chk(y):
    x = y//2
    if y in (0,1):              
        print('not a valid input')
        return None
    if y<0:
        print('ops cannot continue')
        return None
    while x>1:
        if y%x == 0:
            print(y, 'has factor',x)
            break
        x-=1
    else:
        print(y, 'is prime')
    #return y``