from person import Person, Manager

bob = Person('Bob Smith','dev',pay=10000)
tom = Manager('Tom Jones',pay=10000,hobby='Tennis')
sue = Person('Sue Davis','staff',12000)


#importing the shelve module to store the above as a database

import shelve
db = shelve.open('persondb')   #Filename where it has to be stored
for object in (bob,sue,tom):   #Use obj names as attr key
    db[object.name] = object   #Store object in shelve as key
db.close()                     #close the database after making changes


