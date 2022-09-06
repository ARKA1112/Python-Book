#same interact file but using the try statement
while True:
    reply = input("Enter: ")
    if reply == 'stop': break
    else:
        try:
            num = int(reply)
        except:
            print("Bad!"*8)
        else:
            print(num**8)
print('Bye!')
