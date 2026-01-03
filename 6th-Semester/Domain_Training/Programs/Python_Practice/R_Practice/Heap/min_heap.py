import heapq

min_heap = []
numbers = [2,5,7,12,88,11,66,12,44,13]

for i in numbers:
    heapq.heappush(min_heap,i)
print(min_heap)
heapq.heappop(min_heap)
# For sorting
while(min_heap):
    print(heapq.heappop(min_heap),end = " ")