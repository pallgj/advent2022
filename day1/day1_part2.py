import heapq
data = open('input')

currentsum = 0
maxsums = [0, 0, 0]
for line in data:
    value = line.split('\n')[0]
    if value:
        currentsum += int(value)
    else:
        minval = heapq.heappop(maxsums)
        heapq.heappush(maxsums, max(minval, currentsum))
        currentsum = 0
print(sum(maxsums))