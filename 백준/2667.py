# updated: 240817
import sys

input = sys.stdin.readline

n = int(input())
MAP = [input() for _ in range(n)]
visited = [[False] * n for _ in range(n)]


def dfs(cy, cx, vis):
    global cnt
    cnt += 1
    vis[cy][cx] = True

    for dy, dx in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        if 0 <= cx + dx < n and 0 <= cy + dy < n and not vis[cy + dy][cx + dx] and MAP[cy + dy][cx + dx] == '1':
            dfs(cy + dy, cx + dx, vis)


counts = []
total = 0
for y in range(n):
    for x in range(n):
        if MAP[y][x] == '1' and not visited[y][x]:
            cnt = 0
            dfs(y, x, visited)
            counts.append(cnt)
            total += 1

counts.sort()
print(total)
print(*counts, end='\n')
