#백준 18405번
#틀렸,, 디버깅 필요
from collections import deque

def solution(n, matrix, s, x, y):
    lst = list()
    for i in range(n):
        for j in range(n):
            if matrix[i][j] > 0:
                lst.append([matrix[i][j], i, j, 0]) 
    lst.sort()
    queue = deque(lst)
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    while queue:
        v, cx, cy, d = queue.popleft()
        if d > s:
            break
        for dx, dy in dirs:
            if 0 <= cx + dx < n and 0 <= cy + dy < n and matrix[cx+dx][cy+dy] == 0:
                queue.append([v, cx+dx, cy+dy, d + 1])
                matrix[cx+dx][cy+dy] = v
    return matrix[x-1][y-1]

n, k = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
s, x, y = map(int, input().split())
print(solution(n, matrix, s, x, y))