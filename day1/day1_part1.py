data = open('input')

currentsum, maxsum = 0, 0
for line in data:
    value = line.split('\n')[0]
    if value:
        currentsum += int(value)
    else:
        maxsum = max(maxsum, currentsum)
        currentsum = 0
print(maxsum)