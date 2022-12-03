fileName = input('Input:\n')

with open(fileName, 'r') as f:
    sacks = f.readlines()

lookup = ' abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

total = 0

loopcount = 0

while loopcount < len(sacks):
    badge = set(sacks[loopcount]).intersection(set(sacks[loopcount + 1]), set(sacks[loopcount + 2]))
    badge.discard('\n')
    total += lookup.index(str(badge)[2])
    loopcount += 3

print(total)