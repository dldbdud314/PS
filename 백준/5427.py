"""
5427. 불
** BFS
"""
from collections import deque


def bfs(board, n, m):
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    # 불 위치 넣고 나서 상근 위치 넣은 큐
    queue = deque([])
    sx, sy = None, None  # 상근 위치
    for i in range(n):
        for j in range(m):
            if board[i][j] == '*':
                queue.append((i, j, -1))
            elif board[i][j] == '@':
                sx, sy = i, j
                board[i][j] = '.'
    queue.append((sx, sy, 0))  # 상근 위치 마지막에

    # bfs
    visited = [[False] * m for _ in range(n)]
    visited[sx][sy] = True
    while queue:
        cx, cy, dis = queue.popleft()

        if dis >= 0 and board[cx][cy] == '0':
            return dis

        # 불
        if dis == -1:
            for dx, dy in dirs:
                if board[cx + dx][cy + dy] == '.':
                    queue.append((cx + dx, cy + dy, -1))
                    board[cx + dx][cy + dy] = '*'
        else:
            for dx, dy in dirs:
                if (board[cx + dx][cy + dy] == '.' or board[cx + dx][cy + dy] == '0') and not visited[cx + dx][cy + dy]:
                    queue.append((cx + dx, cy + dy, dis + 1))
                    visited[cx + dx][cy + dy] = True

    return "IMPOSSIBLE"


T = int(input())
for _ in range(T):
    m1, n1 = map(int, input().split())
    board = [['0'] * (m1 + 2) for _ in range(n1 + 2)]  # 최외각 '0'
    input_b = [input() for _ in range(n1)]

    # copy board
    for i in range(n1):
        for j in range(m1):
            board[i + 1][j + 1] = input_b[i][j]

    print(bfs(board, n1 + 2, m1 + 2))
