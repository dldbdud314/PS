# 방문 처리는 비용으로! -> 더 적은 비용으로 갱신 !
# TC 25번 fail
# dp에 방향 정보도 포함되어야..?
from collections import deque


def solution(board):
    end = len(board) - 1
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    queue = deque([(0, 0, -1, 0)])  # x, y, d, c
    visited = [[-1] * len(board) for _ in range(len(board))]  # 비용
    visited[0][0] = 0

    min_cost = float('inf')
    while queue:
        x, y, d, c = queue.popleft()

        if d == -1:  # 시작점이면 오른쪽, 아래만 처리하고 넘어갈 것
            if visited[x + 1][y] == -1 and board[x + 1][y] == 0:
                queue.append((x + 1, y, 1, 100))
                visited[x + 1][y] = 100
            if visited[x][y + 1] == -1 and board[x][y + 1] == 0:
                queue.append((x, y + 1, 0, 100))
                visited[x][y + 1] = 100
            continue

        if x == end and y == end:
            min_cost = min(min_cost, c)
            continue

        cur_d = d  # 기존 방향 = d
        for _ in range(4):
            next_x = x + dirs[cur_d][0]
            next_y = y + dirs[cur_d][1]
            if 0 <= next_x < len(board) and 0 <= next_y < len(board) and board[next_x][next_y] == 0:
                cost = c + 100 if cur_d == d else c + 600
                if visited[next_x][next_y] == -1 or visited[next_x][next_y] >= cost:
                    queue.append((next_x, next_y, cur_d, cost))
                    visited[next_x][next_y] = cost
            cur_d = cur_d + 1 if cur_d + 1 < 4 else 0

    return min_cost


# print(solution([[0, 0, 0], [0, 0, 0], [0, 0, 0]]))
# print(solution([[0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0],
#                 [0, 0, 0, 1, 0, 0, 0, 1], [0, 0, 1, 0, 0, 0, 1, 0], [0, 1, 0, 0, 0, 1, 0, 0],
#                 [1, 0, 0, 0, 0, 0, 0, 0]]))
# print(solution([[0, 0, 1, 0], [0, 0, 0, 0], [0, 1, 0, 1], [1, 0, 0, 0]]))
# print(solution([[0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 0], [0, 0, 1, 0, 0, 0], [1, 0, 0, 1, 0, 1], [0, 1, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0]]))
# print(solution([[0, 0, 0, 0, 0, 0, 0, 0], [1, 0, 1, 1, 1, 1, 1, 0], [1, 0, 0, 1, 0, 0, 0, 0], [1, 1, 0, 0, 0, 1, 1, 1],
#                 [1, 1, 1, 1, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 0], [1, 1, 1, 1, 1, 1, 1, 0],
#                 [1, 1, 1, 1, 1, 1, 1, 0]]))