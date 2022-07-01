from _heapq import heappop, heappush

def solution(operations):
    min_heap = []
    max_heap = []
    size = 0 #배열 크기 따로 관리
    for op in operations:
        ins, num = op.split()
        num = int(num)
        if ins == 'I':
            heappush(min_heap, num)
            heappush(max_heap, (-num, num))
            size += 1
        else:
            if size == 0: continue
            if num == -1: heappop(min_heap)
            else: heappop(max_heap)
            size -= 1
    if size > 0:
        lst = []
        for x in min_heap:
            if (-x, x) in max_heap:
                lst.append(x)
        return [max(lst), min(lst)]
    return [0, 0]