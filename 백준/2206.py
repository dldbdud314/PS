"""
2206. 벽 부수고 이동하기
** BFS
"""
from collections import deque


n, m = map(int, input().split())
board = [input() for _ in range(n)]


def bfs():
    queue = deque([(0, 0, 1, False)])
    # 벽을 뚫고 방문한 전적이 있냐 / 벽을 뚫지 않고 방문한 전적이 있냐
    visited = [[[False] * 2 for _ in range(m)] for _ in range(n)]

    while queue:
        cx, cy, d, flag = queue.popleft()

        if (cx, cy) == (n - 1, m - 1):
            return d

        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            if 0 <= cx + dx < n and 0 <= cy + dy < m and not visited[cx + dx][cy + dy][int(flag)]:
                if flag and board[cx + dx][cy + dy] == '1':
                    continue
                queue.append((cx + dx, cy + dy, d + 1, flag or board[cx + dx][cy + dy] == '1'))
                visited[cx + dx][cy + dy][int(flag)] = True

    return -1


print(bfs())

