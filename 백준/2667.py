#단지번호붙이기

def dfs(x, y, matrix, visited):
    if 0 > x or x >= len(matrix) or 0 > y or y >= len(matrix):
        return
    if matrix[x][y] == 0 or visited[x][y]:
        return
    
    visited[x][y] = True
    dirs = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    for dx, dy in dirs:
        dfs(x+dx, y+dy, matrix, visited)

def get_counts(n, matrix):
    visited = [[False] * n for _ in range(n)]
    #house_cnt = []
    for i in range(n):
        for j in range(n):
            cnt = 0
            if matrix[i][j] == 1 and not visited[i][j]: 
                dfs(i, j, matrix, visited)
                cnt += 1
    return cnt

n = int(input())
matrix = [list(map(int, input())) for _ in range(n)]
print(get_counts(n, matrix))