"""
1937. 욕심쟁이 판다
** DFS + DP -> 시간초과, 풀이 수정 필요 .. !!
"""
import sys
sys.setrecursionlimit(10 ** 6)

input = sys.stdin.readline


def dfs(cx, cy, cnt):
    dp[cx][cy] = cnt

    for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        if 0 <= cx + dx < n and 0 <= cy + dy < n and MAP[cx + dx][cy + dy] < MAP[cx][cy] and dp[cx + dx][cy + dy] < cnt + 1:
            dfs(cx + dx, cy + dy, cnt + 1)


n = int(input())
MAP = [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if dp[i][j] == 0:
            dfs(i, j, 1)

res = 0
for x in dp:
    res = max(max(x), res)

print(res)
