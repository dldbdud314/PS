"""
** DFS
"""
import sys
sys.setrecursionlimit(10**5)


def dfs(n, m, cx, cy, v, maps, colors):
    colors.append(int(maps[cx][cy]))

    for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        if 0 <= cx + dx < n and 0 <= cy + dy < m and not v[cx + dx][cy + dy] and maps[cx + dx][cy + dy] != 'X':
            v[cx + dx][cy + dy] = True
            dfs(n, m, cx + dx, cy + dy, v, maps, colors)

    return sum(colors)


def solution(maps):
    n, m = len(maps), len(maps[0])
    visited = [[False] * m for _ in range(n)]
    islands = []
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and maps[i][j] != 'X':
                visited[i][j] = True
                islands.append(dfs(n, m, i, j, visited, maps, []))

    if not islands:
        return [-1]

    return sorted(islands)


print(solution(["X591X", "X1X5X", "X231X", "1XXX1"]))
