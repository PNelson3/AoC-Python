fileName = input('Input:\n')

with open(fileName, 'r') as f:
    games = f.readlines()

total = 0

for i in games:
    if i[0] == 'A' and i[2] == 'X': total += 3
    elif i[0] == 'A' and i[2] == 'Y': total += 4
    elif i[0] == 'A' and i[2] == 'Z': total += 8
    elif i[0] == 'B' and i[2] == 'X': total += 1
    elif i[0] == 'B' and i[2] == 'Y': total += 5
    elif i[0] == 'B' and i[2] == 'Z': total += 9
    elif i[0] == 'C' and i[2] == 'X': total += 2
    elif i[0] == 'C' and i[2] == 'Y': total += 6
    else: total += 7

print(total)