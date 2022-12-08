fileName = input('Input:\n')

with open(fileName, 'r') as f:
    instructions = f.readlines()

directories = {'/': 0}
current = ['']

def pathKey(folders: list) -> str:
    pathKey = ''
    for i in folders:
        pathKey = pathKey + i + '/'
    return pathKey

ans = 90000000

for i in instructions:
    i = i[:-1].split(' ')
    if i[0] == '$':
        if i[1] == 'cd':
            if i[2] == '/':
                current = ['']
            elif (i[2] == '..'):
                if len(current) > 1:
                    current.pop()
            else:
                current.append(i[2])
    elif i[0] == 'dir':
        path = pathKey(current) + i[1] + '/'
        directories.update({path: 0})
    else:
        d = 0
        while d < len(current):
            path = ''
            if d == 0:
                path = pathKey(current)
            else:
                path = pathKey(current[:(-1 * d)])
            directories.update({path: directories.get(path) + int(i[0])})
            d += 1

freeSpace = 70000000 - directories.get('/')
print(directories.get('/'))
print(freeSpace)
for dir in directories.values():
    if (dir < ans) and (freeSpace + dir > 30000000):
        ans = dir

print(ans)