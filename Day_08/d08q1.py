import numpy as np

fileName = input('Input:\n')

with open(fileName, 'r') as f:
    lines = f.readlines()

trees = list()

y = 0

for i in lines:
    trees.append(list())
    for c in i:
        if c == '\n':
            break
        trees[y].append(int(c))
    y += 1

visible = np.zeros((len(trees), len(trees[0])))

y = 0
while y < len(trees):
    x = 0
    while x < len(trees[0]):
        height = trees[y][x]
        if (y == 0) or (x == 0) or (y == len(trees) - 1) or (x == len(trees[0]) - 1):
            visible[y, x] = 1
        else:
            #north
            check = 0
            highest = 0
            while check < y:
                if trees[check][x] > highest: highest = trees[check][x]
                if highest == 9: break
                check += 1
            if height > highest: visible[y, x] = 1
            #south
            check = len(trees) - 1
            highest = 0
            while check > y:
                if trees[check][x] > highest: highest = trees[check][x]
                if highest == 9: break
                check -= 1
            if height > highest: visible[y, x] = 1
            #west
            check = 0
            highest = 0
            while check < x:
                if trees[y][check] > highest: highest = trees[y][check]
                if highest == 9: break
                check += 1
            if height > highest: visible[y, x] = 1
            #east
            check = len(trees[0]) - 1
            highest = 0
            while check > x:
                if trees[y][check] > highest: highest = trees[y][check]
                if highest == 9: break
                check -= 1
            if height > highest: visible[y, x] = 1
        x += 1
    y += 1

print(visible)
print(np.sum(visible))
