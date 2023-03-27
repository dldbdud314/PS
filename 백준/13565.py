"""
13565. 침투
** DFS (floodfill)
"""
import sys
sys.setrecursionlimit(10 ** 6)

n, m = map(int, input().split())
board = [list(input()) for _ in range(n)]


def dfs(cx, cy):
    board[cx][cy] = '2'  # 침투 O
    for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        if 0 <= dx + cx < n and 0 <= dy + cy < m and board[dx + cx][dy + cy] == '0':
            dfs(dx + cx, dy + cy)


# outer side 에서 침투 시작
for k in range(m):
    if board[0][k] == '0':
        dfs(0, k)

# inner side 침투 여부 확인
success = False
for k in range(m):
    if board[n - 1][k] == '2':
        success = True
        break

print("YES" if success else "NO")
