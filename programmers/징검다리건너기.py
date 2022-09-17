#합계: 94.9 / 100.0
def solution(stones, k):
    if len(stones) == 1:
        return stones[0]
    l = 1
    r = max(stones)
    ans = 0
    while l <= r:
        mid = (l + r) // 2
        cnt = 0
        for stone in stones:
            if cnt >= k:
                ans = mid
                r = mid - 1
                break
            if stone - mid <= 0:
                cnt += 1
            else:
                cnt = 0
        else:
            l = mid + 1
    return ans

print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))