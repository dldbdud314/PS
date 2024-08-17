'''
7576. 토마토
** bfs
'''
import sys
from collections import deque

input = sys.stdin.readline

m, n = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(n)]

queue = deque([])
for i in range(n):
    for j in range(m):
        if box[i][j] == 1:
            queue.append((i, j, 0))

time = 0  # 최단 시간 기록용 bfs level
while queue:
    cy, cx, t = queue.popleft()
    time = max(time, t)
    for dy, dx in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        if 0 <= cy + dy < n and 0 <= cx + dx < m and box[cy + dy][cx + dx] == 0:
            queue.append((cy + dy, cx + dx, t + 1))
            box[cy + dy][cx + dx] = 1

print(-1 if any(0 in line for line in box) else time)