#Going nesting in Loop

while True:
    reply = input("enter: ")
    if reply == 'stop': break
    elif not reply.isdigit():
        print('bad!'*8)
    else:
        num = int(reply)
        if num <20:
            print('low')
        else:
            print(num**2)
print('Bye!')