"""
16918. 봄버맨
** 시뮬레이션
"""
r, c, n = map(int, input().split())
board = [list(input()) for _ in range(r)]

# 초기화
for i in range(r):
    for j in range(c):
        if board[i][j] == 'O':
            board[i][j] = 1
        elif board[i][j] == '.':
            board[i][j] = 0


def tick():  # 1초씩 흐르기 (+폭발물 설치)
    for i in range(r):
        for j in range(c):
            board[i][j] += 1


def boom():  # 폭발시키기
    to_explode = set()
    for i in range(r):
        for j in range(c):
            if board[i][j] == 3:
                to_explode.add((i, j))
                for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    if 0 <= i + di < r and 0 <= j + dj < c:
                        to_explode.add((i + di, j + dj))
    for x, y in to_explode:
        board[x][y] = 0


t = 1
while t < n:
    tick()  # 1초++
    t += 1
    if t % 2 == 1:
        boom()  # 폭발

# print board
res_board = []
for i in range(r):
    row = ['.'] * c
    for j in range(c):
        if board[i][j] > 0:
            row[j] = 'O'
    print(''.join(row))
