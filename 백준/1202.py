#보석도둑
#시간초과 
from collections import deque
from heapq import heappush, heappop

def solution(gems, bags):
    gems.sort()
    gem_queue = deque(gems)
    bags.sort()
    total = 0
    heap = []
    #이중루프X - 어떻게 개선할지 모르겠다
    for bag in bags:
        while gem_queue and gem_queue[0][0] <= bag:
            _, price = gem_queue.popleft()
            heappush(heap, (-price, price))
        if not heap: continue
        total += heappop(heap)[1]
        
    return total
        
n, k = map(int, input().split())
gems = [list(map(int, input().split())) for _ in range(n)]
bags = [int(input()) for _ in range(k)]

print(solution(gems, bags))