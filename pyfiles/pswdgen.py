def repeater(num):
    import random
    I = 'abcdefghijklmnopqrtsuvwxyz'
    K = [i for i in I] + [str(i) for i in range(12)]
    random.shuffle(K)
    K = K*num
    J = ''.join(random.sample(K,num))
    print(J)
