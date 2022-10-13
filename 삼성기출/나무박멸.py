from copy import deepcopy

n, m, k, c = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(n)]

def print_arr(arr, n):
    for i in range(n):
        print(arr[i])

def grow(n):
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    for i in range(n):
        for j in range(n):
            if MAP[i][j] > 0:
                for di, dj in dirs:
                    if 0 <= i + di < n and 0 <= j + dj < n and MAP[i+di][j+dj] > 0:
                        MAP[i][j] += 1

def spread(map_copy, n):
    new_map = map_copy
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    for i in range(n):
        for j in range(n):
            if MAP[i][j] > 0:
                spread_pos = []
                for di, dj in dirs:
                    if 0 <= i + di < n and 0 <= j + dj < n and MAP[i+di][j+dj] == 0:
                        spread_pos.append((i + di, j + dj))
                for si, sj in spread_pos:
                    new_map[si][sj] += (MAP[i][j] // len(spread_pos))
    return new_map

def pick_position(n, k):
    dirs = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    records = []
    for i in range(n):
        for j in range(n):
            if MAP[i][j] > 0:
                total = MAP[i][j]
                for di, dj in dirs:
                    for l in range(1, k + 1):
                        if 0 <= i + (di * l) < n and 0 <= j + (dj * l) < n:
                            if MAP[i+(di*l)][j+(dj*l)] > 0:
                                total += MAP[i+(di*l)][j+(dj*l)]
                            else:
                                break
                records.append([(i, j), total]) # 제초제 기록 저장
    if records:
        return sorted(records, key = lambda x : (-x[1], x[0]))[0]
    else:
        return [-1, -1]

def kill_trees(posi, posj, n, k):
    dirs = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    MAP[posi][posj] = -2
    herbicides[posi][posj] = 0
    for di, dj in dirs:
        for l in range(1, k + 1):
            if 0 <= posi + (di * l) < n and 0 <= posj + (dj * l) < n:
                if MAP[posi+(di*l)][posj+(dj*l)] > 0:
                    MAP[posi+(di*l)][posj+(dj*l)] = -2
                    herbicides[posi+(di*l)][posj+(dj*l)] = 0
                elif MAP[posi+(di*l)][posj+(dj*l)] == 0 or MAP[posi+(di*l)][posj+(dj*l)] == -2: # 제초제 칸으로 만들고 탈주 !
                    MAP[posi+(di*l)][posj+(dj*l)] = -2
                    herbicides[posi+(di*l)][posj+(dj*l)] = 0
                    break
                elif MAP[posi+(di*l)][posj+(dj*l)] == -1: # 그냥 탈주 !
                    break

def check_herbicides(n, c):
    for i in range(n):
        for j in range(n):
            if MAP[i][j] == -2: # 제초제 칸에 대해서
                if herbicides[i][j] == c:
                    herbicides[i][j] = 0
                    MAP[i][j] = 0 # 빈칸 만들기
                elif herbicides[i][j] < c:
                    herbicides[i][j] += 1

herbicides = [[0] * n for _ in range(n)]

total = 0
for _ in range(m):
    # 나무 성장
    grow(n)
    # 번식
    MAP = spread(deepcopy(MAP), n)
    # 제초제 작업
    pos, cnt = pick_position(n, k) # 제초제 뿌릴 곳 선정
    if cnt == -1: break
    kill_trees(pos[0], pos[1], n, k)
    total += cnt
    check_herbicides(n, c) # 제초제 햇수, 지도 갱신
    
print(total)

# 수정 : 제초제 뿌린 칸  jump 하면 안되고 빈칸이랑 똑같이 취급해야 함..!