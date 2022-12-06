fileName = input('Input:\n')

with open(fileName, 'r') as f:
    signal = f.readline()

index = 0
while index < len(signal) - 3:
    chain = set()
    chainindex = 0
    while chainindex < 4:
        if signal[index + chainindex] in chain:
            break
        chain.add(signal[index + chainindex])
        chainindex += 1
    if len(chain) == 4:
        break
    index += 1

print(index + 4)