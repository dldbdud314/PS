"""DFS 기본"""
import sys
input = sys.stdin.readline

dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def dfs(ci, cj, visited, cnt):
    visited[ci][cj] = True
    cnt += 1

    for di, dj in dirs:
        if 0 <= di + ci < N and 0 <= dj + cj < N and MAP[di+ci][dj+cj] == '1' and not visited[di+ci][dj+cj]:
            cnt = dfs(di + ci, dj + cj, visited, cnt)

    return cnt


N = int(input())
MAP = [input() for _ in range(N)]

visited = [[False] * N for _ in range(N)]
counts = []
for i in range(N):
    for j in range(N):
        if MAP[i][j] == '1' and not visited[i][j]:
            counts.append(dfs(i, j, visited, 0))

counts.sort()
print(len(counts))
print(*counts, sep='\n')
