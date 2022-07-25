#백준 18428
from itertools import combinations
from copy import deepcopy

def dfs(tx, ty, d, hallway, n):
    if hallway[tx][ty] == 'O':
        return
    hallway[tx][ty] = 'T' #방문 표시
    if d == 0: dx, dy = -1, 0
    elif d == 1: dx, dy = 1, 0
    elif d == 2: dx, dy = 0, 1
    elif d == 3: dx, dy = 0, -1
    if 0 <= tx + dx < n and 0 <= ty + dy < n:
        dfs(tx +dx, ty + dy, d, hallway, n)

def solution(n, hallway_org):
    pos_lst = [] # 빈칸
    t_pos = []
    s_cnt = 0
    for i in range(n):
        for j in range(n):
            if hallway_org[i][j] == 'X':
                pos_lst.append((i, j))
            elif hallway_org[i][j] == 'T':
                t_pos.append((i, j))
            elif hallway_org[i][j] == 'S':
                s_cnt += 1
    for c in combinations(pos_lst, 3):
        hallway = deepcopy(hallway_org)
        for x, y in c:
            hallway[x][y] = 'O'
        for tx, ty in t_pos:
            dfs(tx, ty, 0, hallway, n) #상
            dfs(tx, ty, 1, hallway, n) #하
            dfs(tx, ty, 2, hallway, n) #좌
            dfs(tx, ty, 3, hallway, n) #우
        cnt_tmp = 0
        for i in range(n):
            cnt_tmp += hallway[i].count('S')
        if cnt_tmp == s_cnt:
            return "YES"
    return "NO"

n = int(input())
hallway = [input().split() for _ in range(n)]
print(solution(n, hallway))