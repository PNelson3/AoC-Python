fileName = input('Input:\n')

with open(fileName, 'r') as f:
    pairs = f.readlines()

total = 0

for i in pairs:
    left = i[:i.index(',')]
    right = i[i.index(',') + 1:]
    ll = int(left[:left.index('-')])
    lh = int(left[left.index('-') + 1:])
    rl = int(right[:right.index('-')])
    rh = int(right[right.index('-') + 1:])
    if (ll <= rh) and (rl <= lh):
        total += 1

print(total)