import sys
from itertools import combinations
from copy import deepcopy
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

def spread_dfs(_matrix, i, j, n, m):
    _matrix[i][j] = 2
    dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    for di, dj in dirs:
        if 0 <= i + di < n and 0 <= j + dj < m and _matrix[i+di][j+dj] == 0:
            spread_dfs(_matrix, i + di, j + dj, n, m)

def get_empty(_matrix, n, m):
    area = 0
    for i in range(n):
        for j in range(m):
            if _matrix[i][j] == 0:
                area += 1
    return area

n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

fires, empties = [], []
for i in range(n):
    for j in range(m):
        if matrix[i][j] == 0:
            empties.append((i, j))
        elif matrix[i][j] == 2:
            fires.append((i, j))

largest = -float('inf')
for positions in combinations(empties, 3):
    _matrix = deepcopy(matrix)
    for _i, _j in positions:
        _matrix[_i][_j] = 1
    for fi, fj in fires:
        spread_dfs(_matrix, fi, fj, n, m)
    largest = max(get_empty(_matrix, n, m), largest)

print(largest)    