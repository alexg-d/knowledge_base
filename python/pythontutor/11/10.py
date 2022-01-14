# Ivanov:
# envelope 5
# marker 3
# paper 17

# Petrov:
# envelope 20
# pens 5

# import fileinput
from sys import stdin

db = {}

for line in stdin.readlines():
    name, good, count = line.split()
    db[name] = db.get(name, {})
    db[name][good] = db[name].get(good, 0) + int(count)

for name, good in sorted(db.items()):
    print(name + ': ')
    for good_key, good_val in sorted(good.items()):
        print(good_key, good_val)

# print(db)


from collections import defaultdict
from sys import stdin

clients = defaultdict(lambda: defaultdict(int))
for line in stdin.readlines():
    client, thing, value = line.split()
    clients[client][thing] += int(value)
        
for client in sorted(clients):
    print(client + ':')
    for thing in sorted(clients[client]):
        print(thing, clients[client][thing])