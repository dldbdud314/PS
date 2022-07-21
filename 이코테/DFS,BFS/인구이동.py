#백준 16234
import sys
sys.setrecursionlimit(10**6) #재귀호출 제한 늘리기

total = 0
flag = False #인구이동 일어나는지 check

def dfs(x, y, n, lands, l, r, visited, pos_lst):
    visited[x][y] = True
    pos_lst.append([x, y])
    global total
    total += lands[x][y]
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    for dx, dy in dirs:
        if 0 <= x + dx < n and 0 <= y + dy < n and not visited[x+dx][y+dy]:
            if l <= abs(lands[x+dx][y+dy] - lands[x][y]) <= r:
                global flag
                flag = True #인구이동이 일어나는 경우
                dfs(x + dx, y + dy, n, lands, l, r, visited, pos_lst)

def solution(n, l, r, lands):
    days = 0
    while True:
        global flag 
        flag = False
        visited = [[False] * n for _ in range(n)]
        pos_lst = []
        for i in range(n):
            for j in range(n):
                if not visited[i][j]:
                    global total
                    dfs(i, j, n, lands, l, r, visited, pos_lst)
                    if flag: #인구 이동이 가능한 경우
                        v = total // len(pos_lst)
                        for x, y in pos_lst:
                            lands[x][y] = v
                    pos_lst = [] #다시 초기화
                    total = 0
        if not flag: break
        days += 1
    return days

n, l, r = map(int, input().split())
lands = [list(map(int, input().split())) for _ in range(n)]
print(solution(n, l, r, lands))