from copy import deepcopy

n, m, k, c = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(n)]

def grow(MAP, n):
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    for i in range(n):
        for j in range(n):
            if MAP[i][j] > 0:
                for di, dj in dirs:
                    if 0 <= i + di < n and 0 <= j + dj < n and MAP[i+di][j+dj] > 0:
                        MAP[i][j] += 1

def spread(org_map, map_copy, n):
    MAP = map_copy
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    for i in range(n):
        for j in range(n):
            if org_map[i][j] > 0:
                spread_pos = []
                for di, dj in dirs:
                    if 0 <= i + di < n and 0 <= j + dj < n and org_map[i+di][j+dj] == 0:
                        spread_pos.append((i + di, j + dj))
                for si, sj in spread_pos:
                    MAP[si][sj] += (org_map[i][j] // len(spread_pos))
    return MAP

def pick_position(MAP, n, k):
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
                            elif MAP[i+(di*l)][j+(dj*l)] == -2: # 제초제 뿌린 칸
                                continue
                            else:
                                break
                records.append([(i, j), total]) # 제초제 기록 저장
    if records:
        return sorted(records, key = lambda x : (-x[1], x[0]))[0]
    else:
        return [-1, -1]

def kill_trees(posi, posj, MAP, herbicides, n, k):
    dirs = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    MAP[posi][posj] = -2
    herbicides[posi][posj] = 0
    for di, dj in dirs:
        for l in range(1, k + 1):
            if 0 <= posi + (di * l) < n and 0 <= posj + (dj * l) < n:
                if MAP[posi+(di*l)][posj+(dj*l)] > 0:
                    MAP[posi+(di*l)][posj+(dj*l)] = -2
                    herbicides[posi+(di*l)][posj+(dj*l)] = 0
                elif MAP[posi+(di*l)][posj+(dj*l)] == 0: # 제초제 칸으로 만들고 탈주 !
                    MAP[posi+(di*l)][posj+(dj*l)] = -2
                    herbicides[posi+(di*l)][posj+(dj*l)] = 0
                    break
                elif MAP[posi+(di*l)][posj+(dj*l)] == -1: # 그냥 탈주 !
                    break
                elif MAP[posi+(di*l)][posj+(dj*l)] == -2: # 제초제가 있던 칸
                    herbicides[posi+(di*l)][posj+(dj*l)] = 0 # 제초제 햇수 reset

def check_herbicides(herbicides, n, c):
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
    grow(MAP, n)
    # 번식
    MAP = spread(MAP, deepcopy(MAP), n)
    # 제초제 작업
    pos, cnt = pick_position(MAP, n, k) # 제초제 뿌릴 곳 선정
    if cnt == -1: break
    kill_trees(pos[0], pos[1], MAP, herbicides, n, k)
    total += cnt
    check_herbicides(herbicides, n, c) # 제초제 햇수, 지도 갱신
    
print(total)

# 실패

# TC 1
# 5 4 5 5
# 0 0 0 0 0 
# 0 0 0 -1 1 
# 0 0 5 0 0 
# 4 0 0 0 0 
# 2 0 -1 0 0
# 정답 : 33 / 출력 : 34

# TC 2
# 11 446 20 3
# 0 0 0 -1 57 0 -1 0 0 0 0 
# 0 18 0 -1 -1 0 0 0 0 0 45 
# 64 0 10 0 0 -1 74 0 0 33 0 
# 0 61 0 0 -1 0 0 0 0 0 -1 
# 0 66 0 0 0 0 0 0 16 0 0 
# 7 0 0 0 6 0 0 -1 27 72 0 
# 0 0 0 0 0 54 0 42 -1 -1 0 
# 0 0 -1 0 0 0 0 1 0 0 98 
# -1 98 68 0 0 75 1 93 0 0 0 
# 0 0 0 0 77 0 0 -1 0 0 0 
# 0 -1 0 -1 0 0 0 0 45 0 0
# 정답 : 663822