"""
4179. 불 !
- 시뮬 (bfs) : 1. 불 퍼뜨리기 2. 지훈 움직이기 (bfs 2번)
"""
import sys
from collections import deque

input = sys.stdin.readline

r, c = map(int, input().split())
board = [list(input()) for _ in range(r)]

# 지훈 위치 기록 + 불 위치 큐에 넣기
fq = deque([])

jx, jy = None, None
for i in range(r):
    for j in range(c):
        if board[i][j] == 'J':
            jx, jy = i + 1, j + 1
            board[i][j] = '.'
        elif board[i][j] == 'F':
            fq.append((i + 1, j + 1, 0))
            board[i][j] = '0'

# 테두리 'x' 처리
nboard = [['x'] * (c + 2) for _ in range(r + 2)]
for i in range(r):
    for j in range(c):
        nboard[i + 1][j + 1] = board[i][j]


def spread():  # 시간 만큼 불 위치 표시
    while fq:
        cx, cy, d = fq.popleft()

        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            if nboard[cx + dx][cy + dy] == '.':
                nboard[cx + dx][cy + dy] = str(d + 1)
                fq.append((cx + dx, cy + dy, d + 1))


def move():  # (현재 시간 <= 불 시간) -> 지훈 이동
    jq = deque([(jx, jy, 0)])

    visited = [[False] * (c + 2) for _ in range(r + 2)]
    visited[jx][jy] = True

    while jq:
        cx, cy, d = jq.popleft()

        if nboard[cx][cy] == 'x':
            return d

        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            if nboard[cx + dx][cy + dy] == '#':
                continue
            if (nboard[cx + dx][cy + dy] in {'.', 'x'} or d + 1 < int(nboard[cx + dx][cy + dy])) and not visited[cx + dx][cy + dy]:
                visited[cx + dx][cy + dy] = True
                jq.append((cx + dx, cy + dy, d + 1))

    return -1


spread()
res = move()

print("IMPOSSIBLE" if res == -1 else res)
