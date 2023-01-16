n, m = map(int, input().split())
MATRIX = [list(map(int, input().split())) for _ in range(n)]


def define_block_groups(cur_block_group, v, x, y, color):
    v[x][y] = True
    cur_block_group.append((x, y))
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    for dx, dy in dirs:
        if 0 <= x + dx < n and 0 <= y + dy < n and MATRIX[x + dx][y + dy] >= 0 and not v[x + dx][y + dy]:
            if 0 < MATRIX[x + dx][y + dy] == color:  # 기준 컬러와 동일
                define_block_groups(cur_block_group, v, x + dx, y + dy, color)
            elif MATRIX[x + dx][y + dy] == 0:  # 다음 컬러가 0이라면 상관 없이 탐색
                define_block_groups(cur_block_group, v, x + dx, y + dy, color)


def init_visited(visited):
    for i in range(n):
        for j in range(n):
            if MATRIX[i][j] == 0:
                visited[i][j] = False


def find_block_groups():
    groups = []
    visited = [[False] * n for _ in range(n)]  # 무지개 블록 방문 표시 해제 알아보기..
    for i in range(n):
        for j in range(n):
            if not visited[i][j] and MATRIX[i][j] > 0:
                cur_block_group = []
                define_block_groups(cur_block_group, visited, i, j, MATRIX[i][j])
                if len(cur_block_group) >= 2:
                    groups.append(cur_block_group)
                init_visited(visited)  # 0인 애들 reset (무지개는 방문 여부 상관없이 또 방문할 수 있어야 함)
    return groups


def get_block_record(block_idx, cur_group):
    size = len(cur_group)  # 블록 그룹 크기
    rainbow_cnt = 0  # 무지개 블록 개수
    std_block = -1  # 기준 블록 위치
    for i, j in cur_group:
        if MATRIX[i][j] == 0:
            rainbow_cnt += 1
        elif MATRIX[i][j] > 0 and std_block == -1:
            std_block = (i, j)
    return [size, rainbow_cnt, std_block, block_idx]


def eliminate_max_group(max_group):
    for i, j in max_group:
        MATRIX[i][j] = -2  # 빈칸
    return len(max_group) * len(max_group)


def gravity_fall():
    for j in range(n):
        for i in range(n - 1, -1, -1):
            flag = False  # 밑에 빈칸 있으면 True
            if MATRIX[i][j] >= 0:
                # 밑에 블록이 없는 경우 drop !
                if i + 1 < n:
                    k = i + 1
                    while k < n and MATRIX[k][j] == -2:
                        flag = True
                        k += 1
                    if flag:
                        MATRIX[k - 1][j] = MATRIX[i][j]
                        MATRIX[i][j] = -2


def turn_anticlockwise():
    after_turn = [[0] * n for _ in range(n)]
    tmp_matrix = []

    for i in range(n):
        tmp = []
        for j in range(n - 1, -1, -1):
            tmp.append(MATRIX[i][j])
        tmp_matrix.append(tmp)

    for j in range(n):
        for i in range(n):
            after_turn[i][j] = tmp_matrix[j][i]

    return after_turn


total_score = 0
while True:
    block_groups = find_block_groups()
    if not block_groups:  # 블록 그룹이 없는 경우 프로그램 종료
        break
    else:
        # 조건에 부합하는 그룹 찾기
        group_records = []
        for idx, block_group in enumerate(block_groups):
            group_records.append(get_block_record(idx, block_group))
        group_records.sort(reverse=True)
        max_group_idx = group_records[0][3]
        # 해당 그룹 빈칸으로 만들고 점수 갱신
        total_score += eliminate_max_group(block_groups[max_group_idx])
        gravity_fall()  # 중력
        MATRIX = turn_anticlockwise()
        gravity_fall()

print(total_score)
