def addDict(dict1, dict2):
    if type(dict1) == dict:
        A = {}
        for x in dict1.keys():
            for y in dict2.keys():
                if x == y:
                    A[x] = dict1[x]
                else:
                    A[x] = dict1[x]
                    A[y] = dict2[y]
        return A
    else:
        A = []
        for x in dict1:
            A.append(x)
        for y in dict2:
            A.append(y)
    A = set(A)               #assigning to set to remove the duplicates
    A = list(A)
    return A
