"""
17836. 공주님을 구해라!

** BFS - 맞왜틀..
"""
import sys
from collections import deque

input = sys.stdin.readline
dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def bfs():
    visited = [[False] * m for _ in range(m)]
    queue = deque([(0, 0, 0)])
    visited[0][0] = True
    gram_time = float('inf')
    while queue:
        cx, cy, ct = queue.popleft()

        if cx == n - 1 and cy == m - 1:
            return min(ct, gram_time)

        if ct > t:
            break

        if board[cx][cy] == 2:
            gram_time = ct + (n - 1 - cx) + (m - 1 - cy)
            continue

        for dx, dy in dirs:
            if 0 <= cx + dx < n and 0 <= cy + dy < m and not visited[cx + dx][cy + dy] and board[cx + dx][cy + dy] != 1:
                visited[cx + dx][cy + dy] = True
                queue.append((cx + dx, cy + dy, ct + 1))

    return "Fail"


n, m, t = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

print(bfs())
