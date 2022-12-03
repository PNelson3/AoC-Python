fileName = input('Input:\n')

with open(fileName, 'r') as f:
    nums = f.readlines()

largest = 0
elf = 0

for i in nums:
    if i == '\n':
        if largest < elf:
            largest = elf
        elf = 0
        continue

    elf += int(i)

print(largest)
