#연구소
#brute force + DFS(안전영역 계산)

from copy import deepcopy
from itertools import combinations

def dfs(pos, n, m, map):
    x, y = pos
    map[x][y] = 2
    dirs = [[1, 0], [0, -1], [-1, 0], [0, 1]]
    for dx, dy in dirs:
        if 0 <= x + dx < n and 0 <= y + dy < m and map[x+dx][y+dy] == 0:
            dfs([x+dx, y+dy], n, m, map)

def get_safety_zone(x, n, m, map, virus):
    map_copy = deepcopy(map)
    posA, posB, posC = x
    map_copy[posA[0]][posA[1]] = 1
    map_copy[posB[0]][posB[1]] = 1
    map_copy[posC[0]][posC[1]] = 1
    
    for vx, vy in virus:
        dfs([vx, vy], n, m, map_copy) #멀 return 하지? - 안함ㅇㅇ 그냥 map 칠하는겨 - 안 칠해진다..ㅎㅅㅎ
    cnt = 0
    for i in range(n):
        for j in range(m):
            if map_copy[i][j] == 0: cnt += 1
    return cnt
    
def solution(n, m, map):
    empty, virus = [], []
    for i in range(n):
        for j in range(m):
            if map[i][j] == 2: virus.append([i, j])
            elif map[i][j] == 0: empty.append([i, j])

    largest_zone = -float('inf')
    for x in combinations(empty, 3):
        safety_zone = get_safety_zone(x, n, m, map, virus)
        largest_zone = max(largest_zone, safety_zone)
    return largest_zone

n, m = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(n)]
print(solution(n, m, map))