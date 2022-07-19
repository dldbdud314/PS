#음료수 얼려 먹기
def dfs(x, y, ice, visited, n, m):
    visited[x][y] = True
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    for dx, dy in dirs:
        if 0 <= x + dx < n and 0 <= y + dy < m and not visited[x+dx][y+dy] and ice[x+dx][y+dy] == 0:
            dfs(x + dx, y + dy, ice, visited, n, m)

def solution(n, m, ice):
    cnt = 0
    visited = [[False] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and ice[i][j] == 0:
                dfs(i, j, ice, visited, n, m)
                cnt += 1
    return cnt

n, m = map(int, input().split())
ice = [list(map(int, input().split())) for _ in range(n)]
print(solution(n, m, ice))