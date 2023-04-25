'''
** two pointer
- 가장 짧은 부분 수열 갱신해가며 투포인터 수행
'''


def solution(sequence, k):
    n = len(sequence)
    l, r = 0, 0
    total = sequence[0]
    ml, mr = -int(1e9), int(1e9)
    while l <= r < n:
        if total < k and r + 1 < n:
            r += 1
            total += sequence[r]
        else:
            if total == k and r - l + 1 < mr - ml + 1:
                ml, mr = l, r
            total -= sequence[l]
            l += 1

    return [ml, mr]
