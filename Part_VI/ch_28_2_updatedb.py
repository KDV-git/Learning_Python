import shelve

db = shelve.open('persondb')

for key in sorted(db):
    print(key, '=>', db[key])

sue = db['Sue Jones']
sue.give_raise(.10)
db['Sue Jones'] = sue

for key in sorted(db):
    print(key, '=>', db[key])

db.close()
