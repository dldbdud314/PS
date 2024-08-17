'''
14940. 쉬운 최단거리
** bfs
'''
import sys
input = sys.stdin.readline

from collections import deque

n, m = map(int, input().split())
MAP = [[0] * m for _ in range(n)]
dis = [[-1] * m for _ in range(n)]

start = []
for i in range(n):
    row = list(map(int, input().split()))
    for j in range(m):
        if row[j] == 2:
            start = [i, j]
            dis[i][j] = 0
        MAP[i][j] = row[j]

        if MAP[i][j] == 0:
            dis[i][j] = 0

queue = deque([start])
while queue:
    cy, cx = queue.popleft()
    for dy, dx in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        if 0 <= cy + dy < n and 0 <= cx + dx < m and dis[cy + dy][cx + dx] == -1 and MAP[cy + dy][cx + dx] == 1:
            queue.append([cy + dy, cx + dx])
            dis[cy + dy][cx + dx] = dis[cy][cx] + 1

for i in range(n):
    print(*dis[i], sep=" ")