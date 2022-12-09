import numpy as np

fileName = input('Input:\n')

with open(fileName, 'r') as f:
    instructions = f.readlines()

KnotLocs = np.zeros((10, 2))

TailPlaces = set()

for i in instructions:
    i = i[:-1].split(' ')
    for j in range(int(i[1])):
        if i[0] == 'U':
            KnotLocs[0, 1] += 1
        elif i[0] == 'D':
            KnotLocs[0, 1] -= 1
        elif i[0] == 'R':
            KnotLocs[0, 0] += 1
        else:
            KnotLocs[0, 0] -= 1
        for knot in range(9):
            if KnotLocs[knot, 0] == KnotLocs[knot + 1, 0] + 2:
                KnotLocs[knot + 1, 0] += 1
                if KnotLocs[knot, 1] > KnotLocs[knot + 1, 1]:
                    KnotLocs[knot + 1, 1] += 1
                elif KnotLocs[knot, 1] < KnotLocs[knot + 1, 1]:
                    KnotLocs[knot + 1, 1] -= 1
            elif KnotLocs[knot, 0] == KnotLocs[knot + 1, 0] - 2:
                KnotLocs[knot + 1, 0] -= 1
                if KnotLocs[knot, 1] > KnotLocs[knot + 1, 1]:
                    KnotLocs[knot + 1, 1] += 1
                elif KnotLocs[knot, 1] < KnotLocs[knot + 1, 1]:
                    KnotLocs[knot + 1, 1] -= 1
            elif KnotLocs[knot, 1] == KnotLocs[knot + 1, 1] + 2:
                KnotLocs[knot + 1, 1] += 1
                if KnotLocs[knot, 0] > KnotLocs[knot + 1, 0]:
                    KnotLocs[knot + 1, 0] += 1
                elif KnotLocs[knot, 0] < KnotLocs[knot + 1, 0]:
                    KnotLocs[knot + 1, 0] -= 1
            elif KnotLocs[knot, 1] == KnotLocs[knot + 1, 1] - 2:
                KnotLocs[knot + 1, 1] -= 1
                if KnotLocs[knot, 0] > KnotLocs[knot + 1, 0]:
                    KnotLocs[knot + 1, 0] += 1
                elif KnotLocs[knot, 0] < KnotLocs[knot + 1, 0]:
                    KnotLocs[knot + 1, 0] -= 1
        TailPlaces.add(str(KnotLocs[9]))

print(len(TailPlaces))