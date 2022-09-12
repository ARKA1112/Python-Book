L = [1, 2, 4, 8, 16, 32, 64]
X = 5
i = 0
while True:
    if 2**X == L[i]:
        print("found on index {}".format(i))
        break
    else:
        i += 1
else:
    print(X, "not found")
