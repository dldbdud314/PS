def solution(n, times):
    left = min(times)
    right = max(times) * n
    ans = 0
    while left <= right:
        mid = (left + right) // 2
        checked = 0
        for time in times:
            checked += (mid // time)
            if checked >= n:
                break
        if checked >= n:
            ans = mid
            right = mid -1
        else:
            left = mid + 1
    return ans