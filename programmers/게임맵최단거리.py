from collections import deque

def solution(maps):
    n, m = len(maps[0]), len(maps) #가로 갈이 n, 세로 길이 m
    if maps[0][0] == 0 or maps[m-1][n-1] == 0: return -1
    
    visited = [[False]*n for _ in range(m)]
    dirs = [(1, 0), (0, -1), (-1, 0), (0, 1)]
    queue = deque([[0, 0, 1]]) #[y, x](=좌표), l(=이동 거리)
    visited[0][0] = True
    while queue:
        y, x, l = queue.popleft()
        if y == m-1 and x == n-1: 
            return l
        for dx, dy in dirs:
            if 0 <= x+dx < n and 0 <= y+dy < m and maps[y+dy][x+dx]==1 and not visited[y+dy][x+dx]:
                visited[y+dy][x+dx] = True
                queue.append([y+dy, x+dx, l+1])    
    return -1
