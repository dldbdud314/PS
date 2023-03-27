"""
11559. Puyo Puyo
** 구현 !
"""
board = []
for _ in range(12):
    board.append(list(input()))


def dfs(color, cx, cy, colors):
    colors.append((cx, cy))
    for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        if 0 <= cx + dx < 12 and 0 <= cy + dy < 6 and (cx + dx, cy + dy) not in colors and board[cx + dx][cy + dy] == color:
            dfs(color, cx + dx, cy + dy, colors)


def pop_puyo(groups):  # 아래로 떨구기
    for j in range(6):
        tmp = []  # 주워서
        for i in range(11, -1, -1):
            if board[i][j] != '.':
                tmp.append(board[i][j])
                board[i][j] = '.'
        idx = 0  # 도로 담기
        for i in range(11, -1, -1):
            if idx >= len(tmp):
                break
            board[i][j] = tmp[idx]
            idx += 1


def find_puyo():
    color_group = []
    checked = [[False] * 6 for _ in range(12)]
    for i in range(11, -1, -1):
        for j in range(6):
            colors = []
            if board[i][j] != '.' and not checked[i][j]:
                dfs(board[i][j], i, j, colors)  # 4개 이상이 해당 컬러로 인접해 있는지?
                if len(colors) >= 4:
                    for cx, cy in colors:
                        checked[cx][cy] = True
                        board[cx][cy] = "."
                    color_group.append(colors)

    return color_group


pop_cnt = 0
while True:
    groups = find_puyo()
    if not groups:  # 하나도 존재하지 않으면 연쇄 pop 끝
        break
    pop_puyo(groups)
    pop_cnt += 1

print(pop_cnt)
