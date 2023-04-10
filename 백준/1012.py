"""
1012. 유기농 배추
** DFS 기본
"""
import sys

input = sys.stdin.readline


def dfs(cx, cy, vis, MAP, n, m):
    vis[cx][cy] = True

    for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        if 0 <= cx + dx < n and 0 <= cy + dy < m and MAP[cx + dx][cy + dy] == 1 and not vis[cx + dx][cy + dy]:
            dfs(cx + dx, cy + dy, vis, MAP, n, m)


def solution():
    m, n, k = map(int, input().split())

    MAP = [[0] * m for _ in range(n)]
    for _ in range(k):
        y, x = map(int, input().split())
        MAP[x][y] = 1

    cnt = 0
    visited = [[False] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if MAP[i][j] == 1 and not visited[i][j]:
                dfs(i, j, visited, MAP, n, m)
                cnt += 1

    return cnt


t = int(input())
for _ in range(t):
    print(solution())
