import sys

input = sys.stdin.readline

from collections import deque


def bfs(n, sy, sx, ty, tx):
    queue = deque([(sy, sx, 0)])
    visited = [[False] * n for _ in range(n)]
    visited[sy][sx] = True
    while queue:
        cy, cx, cnt = queue.popleft()
        if cy == ty and cx == tx:
            return cnt
        for dy, dx in [(1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2)]:
            if 0 <= dy + cy < n and 0 <= dx + cx < n and not visited[dy + cy][dx + cx]:
                queue.append((dy + cy, dx + cx, cnt + 1))
                visited[dy + cy][dx + cx] = True


T = int(input())
for _ in range(T):
    n = int(input())
    sy, sx = map(int, input().split())
    ty, tx = map(int, input().split())
    print(bfs(n, sy, sx, ty, tx))