from itertools import permutations

def solution(k, dungeons):
    max_cnt = -float('inf')
    for x in permutations(dungeons, len(dungeons)):
        total, cnt = k, 0
        for need, use in x:
            if total >= need:
                total -= use
                cnt += 1
        max_cnt = max(max_cnt, cnt)
    return max_cnt