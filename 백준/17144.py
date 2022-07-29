#미세먼지 안녕!
def print_room(r, room):
    for i in range(r):
        print(room[i])
    print('------------------')
        
def upper_circulate(u, c, room):
    x, y = u[0], u[1]
    for i in range(x, 0, -1):
        if i == x: continue
        room[i][y] = room[i-1][y]
    for j in range(0, c - 1):
        room[0][j] = room[0][j+1]
    for i in range(0, x):
        room[i][c-1] = room[i+1][c-1]
    for j in range(c-1, 0, -1):
        room[x][j] = room[x][j-1]
    room[x][y+1] = 0
    
def lower_circulate(d, r, c, room):
    x, y = d[0], d[1]
    for i in range(x, r-1):
        if i == x: continue
        room[i][y] = room[i+1][y]
    for j in range(0, c-1):
        room[r-1][j] = room[r-1][j+1]
    for i in range(r-1, x, -1):
        room[i][c-1] = room[i-1][c-1]
    for j in range(c-1, 0, -1):
        room[x][j] = room[x][j-1]
    room[x][y+1] = 0

def solution(r, c, t, room):
    circulator = []
    for i in range(r):
        for j in range(c):
            if room[i][j] == -1: circulator.append((i, j))
    u, d = circulator[0], circulator[1]
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    for _ in range(t):
        #1. 미세먼지 위치 기록
        dusts = []
        for i in range(r):
            for j in range(c):
                if room[i][j] > 0: dusts.append((i, j))
        #2. 미세먼지 확산
        total_map = [[0] * c for _ in range(r)]
        for x, y in dusts:
            s = room[x][y] // 5
            dcnt = 0
            for dx, dy in dirs:
                if 0 <= x + dx < r and 0 <= y + dy < c and room[x+dx][y+dy] != -1:
                    total_map[x+dx][y+dy] += s
                    dcnt += 1
            room[x][y] -= s * dcnt
        for i in range(r):
            for j in range(c):
                room[i][j] += total_map[i][j]
        #3. 공기청정기 순환
        upper_circulate(u, c, room)
        lower_circulate(d, r, c, room)
    total = 0
    for i in range(r):
        for j in range(c):
            if room[i][j] > 0: total += room[i][j]
    return total

r, c, t = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(r)]
print(solution(r, c, t, room))