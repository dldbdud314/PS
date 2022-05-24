#N번째큰수

from heapq import heappop, heappush, heappushpop

n = int(input())
heap = []
ans = None
for _ in range(n):
    for x in map(int, input().split()):
        if len(heap) < n:
            heappush(heap, x)
            continue
        top = heap[0]
        if top < x: 
            heappushpop(heap, x)
ans = heappop(heap)
print(ans)