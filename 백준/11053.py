# 가장 긴 증가하는 부분 수열 - DP: O(n^2)
def solution(n, arr):
    dp = [1] * n
    for i in range(n):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)


n = int(input())
arr = list(map(int, input().split()))
print(solution(n, arr))
