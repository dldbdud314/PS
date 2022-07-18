#아기상어
#답은 다 맞는데 시간 초과.. why..
from collections import deque

def bfs_distance(shark_pos, fish_pos, size, matrix):
    n = len(matrix)
    visited = [[False] * n for _ in range(n)]
    visited[shark_pos[0]][shark_pos[1]] = True
    dirs = [(-1, 0), (0, -1), (0, 1), (1, 0)]
    queue = deque([[shark_pos[0], shark_pos[1], 0]])
    while queue:
        x, y, d = queue.popleft()
        if [x, y] == fish_pos:
            return d
        for dx, dy in dirs:
            if 0 <= x + dx < n and 0 <= y + dy < n and not visited[x+dx][y+dy] and matrix[x+dx][y+dy] <= size:
                queue.append([x + dx, y + dy, d + 1])
                visited[x+dx][y+dy] = True
    return -1

def solution(n, matrix):
    #물고기 기록하기
    fishes = []
    pos = [0, 0] #아기상어 초기 위치
    for i in range(n):
        for j in range(n):
            if 1 <= matrix[i][j] <= 6:
                fishes.append([i, j]) #위치 기록
            elif matrix[i][j] == 9:
                pos = [i, j]
    time = 0
    fish_cnt = 0
    size = 2
    while True:
        #print_matrix(n, matrix)
        if fish_cnt == size:
            size += 1
            fish_cnt = 0
        #먹을 수 있는 물고기가 있는지 확인, 해당 물고기 기록
        fish_tmp = [] #먹을 수 있는 물고기덜
        for i, j in fishes:
            if matrix[i][j] < size: fish_tmp.append((i, j))
        if not fish_tmp: 
            return time #먹을 수 있는 물고기가 없다면 break
        #물고기 최단거리 계산하기
        shortest = float('inf') #먹을 물고기까지의 최단거리
        to_eat = [0, 0] #먹을 물고기
        tmp_cnt = 0
        for i, j in fish_tmp:
            d = bfs_distance(pos, [i, j], size, matrix) #최단거리 계산
            if d == -1: #먹을 수 있는 물고기가 있지만 거기까지 이동하지 못하는 경우
                tmp_cnt += 1
            elif d < shortest:
                shortest = d
                to_eat = [i, j]
        if tmp_cnt == len(fish_tmp):
            return time
        #물고기 념
        matrix[pos[0]][pos[1]] = 0 #상어 있던 곳
        time += shortest
        pos = to_eat
        fishes.remove(to_eat)
        matrix[pos[0]][pos[1]] = 0 #상어가 이동한 곳 (먹어벌임)
        fish_cnt += 1

n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
print(solution(n, matrix))