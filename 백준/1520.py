# 내리막길
# 1. 단순 dfs - 시간초과
import sys

sys.setrecursionlimit(10 ** 5)


def dfs_0(i, j, visited):
    visited[i][j] = True
    if (i == m - 1) and (j == n - 1):
        global cnt
        cnt += 1
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    for di, dj in dirs:
        if 0 <= i + di < m and 0 <= j + dj < n and not visited[i + di][j + dj] and arr[i][j] > arr[i + di][j + dj]:
            dfs(i + di, j + dj, m, n, arr, visited)
    visited[i][j] = False


def solution_0():
    visited = [[False] * n for _ in range(m)]
    dfs_0(0, 0, visited)


# 2. dfs + dp : visited 처리를 dp로!
def dfs(i, j):
    if i == m - 1 and j == n - 1:
        return 1

    if dp[i][j] >= 0:  # 탐색한 곳 (dp값 >= 0)
        return dp[i][j]

    dp[i][j] = 0  # 탐색 하지 않은 곳 방문 처리
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    for di, dj in dirs:
        if 0 <= i + di < m and 0 <= j + dj < n and arr[i][j] > arr[i + di][j + dj]:
            dp[i][j] += dfs(i + di, j + dj)

    return dp[i][j]


m, n = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(m)]
# cnt = 0
dp = [[-1] * n for _ in range(m)]
print(dfs(0, 0))
# print(cnt)
