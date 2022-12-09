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

mostScenic = 0

y = 1
h = len(trees)
w = len(trees[0])
while y < h - 1:
    x = 1
    while x < w - 1:
        height = trees[y][x]
        north = 0
        south = 0
        west = 0
        east = 0
        check = y - 1
        while check >= 0:
            north += 1
            if trees[check][x] >= height: break
            check -= 1
        check = y + 1
        while check < h:
            south += 1
            if trees[check][x] >= height: break
            check += 1
        check = x - 1
        while check >= 0:
            west += 1
            if trees[y][check] >= height: break
            check -= 1
        check = x + 1
        while check < w:
            east += 1
            if trees[y][check] >= height: break
            check += 1
        score = north * south * west * east
        if score > mostScenic: mostScenic = score
        x += 1
    y += 1

print(mostScenic)