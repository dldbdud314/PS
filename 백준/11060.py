"""
11060. 점프 점프

** DP (+완탐
- dp[i] : i번째까지 최소 Step 수
- dp[i + (1 ~ MAP[i])] = dp[i] + 1
"""
INF = int(1e9)

n = int(input())
MAP = list(map(int, input().split()))

dp = [INF] * n
dp[0] = 0  # 시작점

# bottom-up
for i in range(n - 1):
    if dp[i] == INF or MAP[i] == 0:  # 도달 X, jump X
        continue
    for j in range(1, MAP[i] + 1):
        if i + j < n:
            dp[i + j] = min(dp[i] + 1, dp[i + j])

print(-1 if dp[-1] == INF else dp[-1])
