fileName = input('Input:\n')

with open(fileName, 'r') as f:
    instructions = f.readlines()

i = 0
first = True
X = 1
sum = 0
for cyclecount in range(1, 221):
    addval = 0
    inst = instructions[i][:-1].split(' ')
    if inst[0] == 'addx':
        if not first:
            addval = int(inst[1])
            i += 1
        first = not first
    else:
        i += 1
    if (cyclecount - 20) % 40 == 0:
        sum += X * cyclecount
        print(X * cyclecount)
    X += addval

print(sum)