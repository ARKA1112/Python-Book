from timeit import timeit


while True:
    reply = input('Enter text: ')
    if reply == 'stop':
        break
    print(int(reply) ** 2)
print('bye')