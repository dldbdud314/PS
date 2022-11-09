# 두 동전
from collections import deque


def solution(n, m, board):
    new_board = []
    start_pos = []
    for i in range(n + 2):
        this_line = ''
        for j in range(m + 2):
            if i == 0 or i == n + 1 or j == 0 or j == m + 1:
                this_line += 'x'
            else:
                if board[i - 1][j - 1] == 'o':
                    start_pos.append((i, j))
                    this_line += '.'
                    continue
                this_line += board[i - 1][j - 1]
        new_board.append(this_line)

    start_x1, start_y1 = start_pos[0]
    start_x2, start_y2 = start_pos[1]
    queue = deque([(start_x1, start_y1, start_x2, start_y2, 0)])
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    while queue:
        x1, y1, x2, y2, l = queue.popleft()
        if l >= 10:
            return -1

        for dx, dy in dirs:
            nextx1, nexty1 = x1 + dx, y1 + dy
            nextx2, nexty2 = x2 + dx, y2 + dy
            # 둘 다 나간 경우
            if new_board[nextx1][nexty1] == 'x' and new_board[nextx2][nexty2] == 'x':
                continue
            # 둘 중 하나만 나간 경우
            if new_board[nextx1][nexty1] == 'x':
                return l + 1
            if new_board[nextx2][nexty2] == 'x':
                return l + 1
            # 둘 다 안 나간 경우 - 하나라도 움직인 경우
            move = [1, 1]
            if new_board[nextx1][nexty1] == '#':
                nextx1, nexty1 = x1, y1
                move[0] = 0
            if new_board[nextx2][nexty2] == '#':
                nextx2, nexty2 = x2, y2
                move[1] = 0
            if move[0] or move[1]:
                queue.append((nextx1, nexty1, nextx2, nexty2, l + 1))

    return -1


n, m = map(int, input().split())
board = []
for _ in range(n):
    board.append(input())
print(solution(n, m, board))
