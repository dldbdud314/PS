# 계단 오르기
def solution(n, stairs):
    dp = [[0] * 3 for _ in range(n + 1)]
    dp[1][1] = stairs[0]
    dp[1][2] = stairs[0]
    for i in range(2, n + 1):
        dp[i][1] = max(dp[i-2]) + stairs[i - 1]
        dp[i][2] = dp[i-1][1] + stairs[i - 1]
    return max(dp[n])


n = int(input())
stairs = []
for _ in range(n):
    stairs.append(int(input()))
print(solution(n, stairs))
