import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 5)

n, m, k = map(int, input().split())
MAP = [[0] * m for _ in range(n)]
for _ in range(k):
    r, c = map(int, input().split())
    MAP[r - 1][c - 1] = 1

max_size = 0
vis = [[False] * m for _ in range(n)]


def dfs(cy, cx):
    vis[cy][cx] = True
    global cnt
    cnt += 1
    for dy, dx in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        if 0 <= dy + cy < n and 0 <= dx + cx < m and not vis[dy + cy][dx + cx] and MAP[dy + cy][dx + cx] == 1:
            dfs(dy + cy, dx + cx)


for i in range(n):
    for j in range(m):
        if not vis[i][j] and MAP[i][j] == 1:
            cnt = 0
            dfs(i, j)
            max_size = max(max_size, cnt)

print(max_size)