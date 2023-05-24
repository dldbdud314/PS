"""
2583. 영역 구하기
** 기본 DFS - floodfill
"""
import sys
sys.setrecursionlimit(10 ** 5)

m, n, k = map(int, input().split())
board = [[0] * m for _ in range(n)]


def dfs(cx, cy):
    global cnt
    cnt += 1
    board[cx][cy] = 1
    for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        if 0 <= cx + dx < n and 0 <= cy + dy < m and board[cx + dx][cy + dy] == 0:
            dfs(cx + dx, cy + dy)


for _ in range(k):  # 주어진 영역 색칠하기
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x1, x2):
        for j in range(y1, y2):
            board[i][j] = 1

res = []
for i in range(n):
    for j in range(m):
        if board[i][j] == 0:
            cnt = 0
            dfs(i, j)  # floodfill
            res.append(cnt)

res.sort()
print(len(res))
print(*res)
