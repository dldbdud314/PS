"""
** DP --> 가장 긴 감소 하는 부분 수열 (LIS 유형)
- dp[i] = max(dp[j] + 1, dp[i]) if arr[j] > arr[i] (0 <= j < i < n)
"""


def lis():
    dp = [1] * n  # dp[i] = i번째까지 가장 긴 감소 하는 수열의 최대 개수
    for i in range(1, n):
        for j in range(i):
            if arr[j] > arr[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    return n - max(dp)  # 열외 시킬 병수 수


n = int(input())
arr = list(map(int, input().split()))
print(lis())
