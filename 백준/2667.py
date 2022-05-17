#단지번호붙이기
cnt = 0

def dfs(x, y, matrix):
    if 0 > x or x >= len(matrix) or 0 > y or y >= len(matrix):
        return
    if matrix[x][y] < 1:
        return
    
    global cnt #전역변수 - 누적하기 위해
    matrix[x][y] = -1
    cnt += 1
    dirs = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    for dx, dy in dirs:
        dfs(x+dx, y+dy, matrix)

def get_counts(n, matrix):
    global cnt #전역변수
    ans = 0
    house_counts = []
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 1: 
                dfs(i, j, matrix)
                ans += 1
                house_counts.append(cnt)
                cnt = 0
    return ans, house_counts

n = int(input())
matrix = [list(map(int, input())) for _ in range(n)]

ans, house_counts = get_counts(n, matrix)
print(ans)
house_counts.sort()
for count in house_counts: print(count) 