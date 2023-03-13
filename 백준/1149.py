"""
1149. RGB 거리

** DP
- 규칙에 맞게 dp 테이블 채우기
"""
import sys
input = sys.stdin.readline

INF = int(1e9)


def solution():
    dp = [[INF, INF, INF] for _ in range(n)]
    dp[0] = cost[0]
    for i in range(1, n):
        dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + cost[i][0]
        dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + cost[i][1]
        dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + cost[i][2]

    return min(dp[-1])


n = int(input())
cost = []
for _ in range(n):
    cost.append(list(map(int, input().split())))

print(solution())
