"""
10026. 적록색약
** 기본 DFS
"""
import sys
sys.setrecursionlimit(10 ** 6)

n = int(input())
board = [input() for _ in range(n)]


def dfs1(cx, cy, cur):  # 적록색약 X-DFS
    vis1[cx][cy] = True
    for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        if 0 <= cx + dx < n and 0 <= cy + dy < n and not vis1[cx + dx][cy + dy] and board[cx + dx][cy + dy] == cur:
            dfs1(cx + dx, cy + dy, cur)


vis1 = [[False] * n for _ in range(n)]
cnt1 = 0
# 적록색약X
for i in range(n):
    for j in range(n):
        if not vis1[i][j]:
            dfs1(i, j, board[i][j])
            cnt1 += 1


def dfs2(cx, cy, cur):  # 적록색약-DFS
    vis2[cx][cy] = True
    for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        if 0 <= cx + dx < n and 0 <= cy + dy < n and not vis2[cx + dx][cy + dy]:
            if (cur in 'RG' and board[cx + dx][cy + dy] in 'RG') or cur == board[cx + dx][cy + dy] == 'B':
                dfs2(cx + dx, cy + dy, cur)


vis2 = [[False] * n for _ in range(n)]
cnt2 = 0
# 적록색약O
for i in range(n):
    for j in range(n):
        if not vis2[i][j]:
            dfs2(i, j, board[i][j])
            cnt2 += 1

print(f'{cnt1} {cnt2}')
