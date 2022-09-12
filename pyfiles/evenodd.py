"""
self made programme to check
and print all  the numbers
from the input to the 100
and print the even ones
"""
#Docstrings should always be defined in double quotes
self = input("enter a number ")
try:
    int(self)
except:
    print("input a number")
self = int(self)
cont = []
while self < 100:
    if self % 2 == 0:
        cont.append(self)
        self +=1
    else:
        self+=1
if input("Do you want the numbers? ") == 'y':
    print([i for i in cont])
print("And contains total {} elements".format(len(cont)))