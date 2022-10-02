import shelve
db = shelve.open('persondb')

for key in sorted(db):
    print(key,'\t=>',db[key])

sue = db['Sue Davis']
sue.giveRaise(10)
db['Sue Davis'] = sue
db.close()