fileName = input('Input:\n')

with open(fileName, 'r') as f:
    nums = f.readlines()

largest = [0,0,0]
elf = 0

for i in nums:
    if i == '\n':
        if largest[0] < elf:
            largest[0] = elf
            largest.sort()
        elf = 0
        continue

    elf += int(i)

sum = largest[0] + largest[1] + largest[2]
print(sum)
