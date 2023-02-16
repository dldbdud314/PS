'''
DP
'''


def solution(land):
    n = len(land)
    dp = land[::]
    for i in range(1, n):
        for j in range(4):
            dp[i][j] += max([x for k, x in enumerate(dp[i - 1]) if k != j])  # 바로 윗열 제외

    return max(dp[n - 1])
