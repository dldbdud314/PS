def dfs(i, j, area, arr, cur_num, color):
    area[i][j] = color
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    for di, dj in dirs:
        if 0 <= i + di < n and 0 <= j + dj < n and area[i+di][j+dj] == -1 and cur_num == arr[i+di][j+dj]:
            dfs(i + di, j + dj, area, arr, arr[i+di][j+dj], color)

def calculate_art_score(pos1, pos2, area, arr): #예술 점수 계산
    val1, val2 = arr[pos1[0]][pos1[1]], arr[pos2[0]][pos2[1]] #해당 영역의 값
    a1, a2 = area[pos1[0]][pos1[1]], area[pos2[0]][pos2[1]] #영역
    cnt1, cnt2 = 0, 0 #영역 넓이
    for _i in range(n):
        cnt1 += area[_i].count(a1)
        cnt2 += area[_i].count(a2)
    #맞닿은 변의 개수 구하기
    main_area, other_area = (a2, a1) if cnt1 > cnt2 else (a1, a2) #영역 넓이가 더 작은 데 기준
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    line_count = 0
    for i in range(n):
        for j in range(n):
            if area[i][j] == main_area:
                for di, dj in dirs:
                    if 0 <= i + di < n and 0 <= j + dj < n and area[i+di][j+dj] == other_area:
                        line_count += 1
    
    return (cnt1 + cnt2) * val1 * val2 * line_count

def get_art_score(arr, n):
    # DFS 돌면서 영역 구분하기
    area = [[-1] * n for _ in range(n)] #영역 구분 행렬 (+방문 확인 가능)
    color = 0 #영역 구분 변수
    for i in range(n):
        for j in range(n):
            if area[i][j] == -1:
                dfs(i, j, area, arr, arr[i][j], color)
                color += 1
                
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    # 서로 다른 두 영역에 대한 art score 계산해서 총합
    combination_check = set()
    art_score = 0
    for i in range(n):
        for j in range(n):
            for di, dj in dirs:
                if 0 <= i + di < n and 0 <= j + dj < n and area[i][j] != area[i + di][j + dj]:
                    area1, area2 = area[i][j], area[i + di][j + dj]
                    if (area1, area2) not in combination_check:
                        art_score += calculate_art_score((i, j), (i + di, j + dj), area, arr)
                        combination_check.add((area1, area2)) #조합이므로 순서 상관없이 다 넣기
                        combination_check.add((area2, area1))
    return art_score

def rotate(p, size):
    rotated = [[-1] * size for _ in range(size)]
    for i in range(size):
        for j in range(size):
            rotated[j][size - i - 1] = p[i][j]
    return rotated

def turn_arr(arr, n):
    mid = n // 2

    # 십자가
    tmp = [arr[mid][j] for j in range(n - 1, -1, -1)]
    for i in range(n):
        arr[mid][i] = arr[i][mid]
        arr[i][mid] = tmp[i]

    # 십자가 이외 네 군데
    # 1
    p1 = []
    for i in range(mid):
        p1.append(arr[i][0:mid])
    p1 = rotate(p1, mid)
    for i in range(mid): # 도로 집어넣기
        for j in range(mid):
            arr[i][j] = p1[i][j]
    # 2
    p2 = []
    for i in range(mid):
        p2.append(arr[i][mid+1:])
    p2 = rotate(p2, mid)
    for i in range(mid):
        for j in range(mid):
            arr[i][j + mid + 1] = p2[i][j]
    # 3
    p3 = []
    for i in range(mid + 1, n):
        p3.append(arr[i][0:mid])
    p3 = rotate(p3, mid)
    for i in range(mid): # 도로 집어넣기
        for j in range(mid):
            arr[i + mid + 1][j] = p3[i][j]
    # 4
    p4 = []
    for i in range(mid + 1, n):
        p4.append(arr[i][mid+1:])
    p4 = rotate(p4, mid)
    for i in range(mid):
        for j in range(mid):
            arr[i + mid + 1][j + mid + 1] = p4[i][j]

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

total_score = 0

#초기 예술 점수
total_score += get_art_score(arr, n)

for _ in range(3):
    #회전
    turn_arr(arr, n)
    #예술 점수 구하기
    total_score += get_art_score(arr, n)

print(total_score)