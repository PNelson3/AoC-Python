import numpy as np

fileName = input('Input:\n')

with open(fileName, 'r') as f:
    instructions = f.readlines()

screen = np.zeros((6,40))

i = 0
first = True
X = 1
for pixel in range(240):
    addval = 0
    inst = instructions[i][:-1].split(' ')
    if inst[0] == 'addx':
        if not first:
            addval = int(inst[1])
            i += 1
        first = not first
    else:
        i += 1
    if X-1 <= pixel % 40 <= X+1:
        screen[int(pixel / 40), int(pixel % 40)] = 1
    X += addval

with open("ans.txt", "w") as a:
    ans = str(screen).replace(" ", "")
    ans = ans.replace(".", "")
    ans = ans.replace("[", "")
    ans = ans.replace("]", "")
    ans = ans.replace("0", ".")
    ans = ans.replace("1", "#")
    a.write(ans)