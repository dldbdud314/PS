from bisect import bisect_right

def solution(A, B):
    B.sort()
    taken = [False] * len(B)
    score = 0
    for x in A:
        idx = bisect_right(B, x)
        if idx < len(B):
            for j in range(idx, len(B)):
                if not taken[j]:
                    taken[j] = True
                    score += 1
                    break
    return score