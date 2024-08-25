import sys

input = sys.stdin.readline

from collections import deque

m, n, H = map(int, input().split())
MAP = [[list(map(int, input().split())) for _ in range(n)] for _ in range(H)]

queue = deque([])


def is_ripe():  # 모두 다 익은건지 확인
    for k in range(H):
        for i in range(n):
            for j in range(m):
                if MAP[k][i][j] == 0: return False
    return True


def queue_start():
    for k in range(H):
        for i in range(n):
            for j in range(m):
                if MAP[k][i][j] == 1:
                    queue.append((k, i, j, 0))


def bfs():
    s_time = 0
    while queue:
        ch, cy, cx, t = queue.popleft()
        s_time = t
        for dh, dy, dx in [(0, 0, 1), (0, 1, 0), (0, 0, -1), (0, -1, 0), (1, 0, 0), (-1, 0, 0)]:
            if 0 <= dh + ch < H and 0 <= dy + cy < n and 0 <= dx + cx < m and MAP[dh + ch][dy + cy][dx + cx] == 0:
                queue.append((dh + ch, dy + cy, dx + cx, t + 1))
                MAP[dh + ch][dy + cy][dx + cx] = 1
    return s_time


if is_ripe():
    print(0)
else:
    queue_start()
    t = bfs()
    print(-1) if not is_ripe() else print(t)
