fileName = input('Input:\n')

with open(fileName, 'r') as f:
    sacks = f.readlines()

lookup = ' abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

total = 0

for i in sacks:
    center = int(len(i) /2)
    shared = set(i[:center]).intersection(set(i[center:]))
    total += lookup.index(str(shared)[2])

print(total)