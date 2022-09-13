#안전영역
import sys
sys.setrecursionlimit(10 ** 5)

def dfs(i, j, k, n, heights, visited):
    visited[i][j] = True
    dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    for di, dj in dirs:
        if 0 <= i + di < n and 0 <= j + dj < n and not visited[i+di][j+dj] and heights[i+di][j+dj] > k:
            dfs(i + di, j + dj, k, n, heights, visited)

def solution(n, heights, highest):
    biggest = 1
    for k in range(1, highest):
        visited = [[False] * n for _ in range(n)]
        cnt = 0
        for i in range(n):
            for j in range(n):
                if not visited[i][j] and heights[i][j] > k:
                    dfs(i, j, k, n, heights, visited)
                    cnt += 1
        biggest = max(biggest, cnt)
    return biggest

n = int(input())
heights = []
highest = -float('inf')
for _ in range(n):
    height = list(map(int, input().split()))
    highest = max(max(height), highest)
    heights.append(height)
print(solution(n, heights, highest))