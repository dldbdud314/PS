from heapq import heappush, heappop
def solution(n, works):
    if sum(works) <= n:
        return 0
    #max heap 만들기
    heap = []
    for work in works:
        heappush(heap, (-work, work))
    while n > 0:
        cur = heappop(heap)[1]
        top = heap[0][1]
        if cur == top:
            cur -= 1
            n -= 1
            heappush(heap, (-cur, cur))
            continue
        while n > 0 and cur > top:
            cur -= 1
            n -= 1
        else:
            heappush(heap, (-cur, cur))
    return sum(list(map(lambda x : x[1] * x[1], heap)))
print(solution(3, [1, 1]))