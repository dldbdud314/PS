"""
1937. 욕심쟁이 판다
** DFS + DP -> 수정 : 풀참
"""
import sys
sys.setrecursionlimit(10 ** 6)

input = sys.stdin.readline


def dfs(cx, cy):
    if dp[cx][cy] == 0:
        dp[cx][cy] = 1

        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            if 0 <= cx + dx < n and 0 <= cy + dy < n and MAP[cx + dx][cy + dy] > MAP[cx][cy]:
                dp[cx][cy] = max(dfs(cx + dx, cy + dy), dp[cx][cy])

    return dp[cx][cy] + 1


n = int(input())
MAP = [list(map(int, input().split())) for _ in range(n)]

res = 0
dp = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        res = max(res, dfs(i, j) - 1)

print(res)
