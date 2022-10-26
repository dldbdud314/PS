# 1차) BFS 응용 - 방문 처리 ㅇㅉㅌㅂ..
from collections import deque


def solution(board):
    end = len(board) - 1
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    queue = deque([(0, 0, 0, 0), (0, 0, 1, 0)])  # x, y, d, c
    visited = [[False] * len(board) for _ in range(len(board))]
    visited[0][0] = True

    min_cost = float('inf')
    while queue:
        x, y, d, c = queue.popleft()
        if x == end and y == end:
            min_cost = min(min_cost, c)
            continue

        cur_d = d  # 기존 방향 정보 -> d
        for _ in range(4):
            next_x = x + dirs[cur_d][0]
            next_y = y + dirs[cur_d][1]
            if 0 <= next_x < len(board) and 0 <= next_y < len(board) and not visited[next_x][next_y] and board[next_x][
                next_y] == 0:
                if cur_d == d:
                    queue.append((next_x, next_y, cur_d, c + 100))
                else:
                    queue.append((next_x, next_y, cur_d, c + 600))
                visited[next_x][next_y] = True
            cur_d = cur_d + 1 if cur_d + 1 < 4 else 0

    return min_cost


# print(solution([[0, 0, 0], [0, 0, 0], [0, 0, 0]]))

# print(solution([[0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0],
#                 [0, 0, 0, 1, 0, 0, 0, 1], [0, 0, 1, 0, 0, 0, 1, 0], [0, 1, 0, 0, 0, 1, 0, 0],
#                 [1, 0, 0, 0, 0, 0, 0, 0]]))

# print(solution([[0, 0, 1, 0], [0, 0, 0, 0], [0, 1, 0, 1], [1, 0, 0, 0]]))
# print(solution([[0,0,0,0,0,0],[0,1,1,1,1,0],[0,0,1,0,0,0],[1,0,0,1,0,1],[0,1,0,0,0,1],[0,0,0,0,0,0]]))