fileName = input('Input:\n')

with open(fileName, 'r') as f:
    games = f.readlines()

total = 0

for i in games:
    if i[2] == 'X':
        total += 1
        if i[0] == 'A':
            total += 3
        elif i[0] == 'C':
            total += 6
    elif i[2] == 'Y':
        total += 2
        if i[0] == 'A':
            total += 6
        elif i[0] == 'B':
            total += 3
    else:
        total += 3
        if i[0] == 'B':
            total += 6
        elif i[0] == 'C':
            total += 3

print(total)