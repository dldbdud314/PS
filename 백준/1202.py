#보석도둑
#시간초과.. ha...
from heapq import heappush, heappop, heapify

def solution(gems, bags):
    heapify(gems)
    bags.sort()
    w = 0
    for c in bags:
        tmp_heap = [] #무게를 담는 최대힙
        while gems and gems[0][0] <= c:
            m, v = heappop(gems)
            heappush(tmp_heap, (-v, v, m))
        w += heappop(tmp_heap)[1]
        while tmp_heap: #나머지는 다시 담기
            _, v, m = heappop(tmp_heap)
            heappush(gems, [m, v])
    return w
        
n, k = map(int, input().split())
gems = [list(map(int, input().split())) for _ in range(n)]
bags = [int(input()) for _ in range(k)]
print(solution(gems, bags))