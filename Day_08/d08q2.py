import numpy as np

fileName = input('Input:\n')

with open(fileName, 'r') as f:
    lines = f.readlines()

trees = np.zeros((len(lines), len(lines[0]) - 1))

for i in range(len(lines)):
    for c in range(len(lines[0]) - 1):
        trees[i, c] = int(lines[i][c])

maxScenic = 0
h, w = np.shape(trees)
for y in range(1, h - 1):
    for x in range(1, w - 1):
        height = trees[y, x]
        score = np.zeros(4)
        for i in range(y-1, -1, -1):
            score[0] += 1
            if trees[i, x] >= height: break
        for i in range(y+1, h):
            score[1] += 1
            if trees[i, x] >= height: break
        for i in range(x-1, -1, -1):
            score[2] += 1
            if trees[y, i] >= height: break
        for i in range(x+1, w):
            score[3] += 1
            if trees[y, i] >= height: break
        if np.product(score) > maxScenic: maxScenic = np.product(score)
print(maxScenic)