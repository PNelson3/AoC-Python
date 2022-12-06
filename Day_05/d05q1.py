fileName = input('Input:\n')

with open(fileName, 'r') as f:
    instructions = f.readlines()

stacks = list()

i = 0
while i < 9:
    j = 0
    stack = list()
    while j < 8:
        content = instructions[j][1 + (i * 4)]
        if content != ' ':
            stack.insert(0, content)
        j += 1
    stacks.append(stack)
    i += 1

for inst in instructions:
    if inst[0] != 'm':
        continue
    amount = int(inst[inst.index('move') + 5:inst.index('from') - 1])
    origin = int(inst[inst.index('from') + 5]) - 1
    destination = int(inst[inst.index('to') + 3]) - 1

    print(amount)
    print(origin)
    print(destination)

    moved = 0
    while moved < amount:
        stacks[destination].append(stacks[origin].pop())
        moved += 1

print(stacks)
