import numpy as np

def moveTail(head, tail):
    if head[0] == tail[0] + 2:
        tail[0] += 1
        if head[1] > tail[1]:
            tail[1] += 1
        elif head[1] < tail[1]:
            tail[1] -= 1
    elif head[0] == tail[0] - 2:
        tail[0] -= 1
        if head[1] > tail[1]:
            tail[1] += 1
        elif head[1] < tail[1]:
            tail[1] -= 1
    elif head[1] == tail[1] + 2:
        tail[1] += 1
        if head[0] > tail[0]:
            tail[0] += 1
        elif head[0] < tail[0]:
            tail[0] -= 1
    elif head[1] == tail[1] - 2:
        tail[1] -= 1
        if head[0] > tail[0]:
            tail[0] += 1
        elif head[0] < tail[0]:
            tail[0] -= 1

TailPlaces = set()
fileName = input('Input:\n')

with open(fileName, 'r') as f:
    instructions = f.readlines()

headPos = np.zeros(2)
tailPos = headPos.copy()

for i in instructions:
    i = i[:-1].split(' ')
    for j in range(int(i[1])):
        if i[0] == 'U':
            headPos[1] += 1
        elif i[0] == 'D':
            headPos[1] -= 1
        elif i[0] == 'R':
            headPos[0] += 1
        else:
            headPos[0] -= 1
        moveTail(headPos, tailPos)
        TailPlaces.add(str(tailPos))

print(len(TailPlaces))