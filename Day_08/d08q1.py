import numpy as np

fileName = input('Input:\n')

with open(fileName, 'r') as f:
    lines = f.readlines()

trees = np.zeros((len(lines), len(lines[0]) - 1))
visible = trees.copy()

for i in range(len(lines)):
    for c in range(len(lines[0]) - 1):
        trees[i, c] = int(lines[i][c])

h, w = np.shape(trees)
for y in range(h):
    for x in range(w):
        height = trees[y, x]
        if y == 0 or x == 0 or y == h - 1 or x == w - 1:
            visible[y, x] = 1
        else:
            highest_north = np.max(trees[:y, x])
            highest_south = np.max(trees[y+1:, x])
            highest_west = np.max(trees[y, :x])
            highest_east = np.max(trees[y, x+1:])
            if height > min(highest_north, highest_south, highest_west, highest_east):
                visible[y, x] = 1

print(np.sum(visible))