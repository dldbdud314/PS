'''
방법1. 완전탐색

- 2 * 2 일치하는 블록 찾아서 표시한다('0') ---> 이부분과
- '0' 개수 세서 update
- 블록 떨구기 ---> 이부분이
    - 역순으로 리스트에 담은 뒤 재배치해서 return

비효율적인 기분,,
'''
def color_four_blocks(m, n, board):
    # 위치 확인 먼저, (시작점 기준으로 기록)
    to_color = []
    for i in range(m - 1):
        for j in range(n - 1):
            if board[i][j] is None:
                continue
            if board[i][j] == board[i][j + 1] == board[i + 1][j] == board[i + 1][j + 1] != '0':
                to_color.append([i, j])
                # 후 색칠
    for i, j in to_color:
        board[i][j] = board[i][j + 1] = board[i + 1][j] = board[i + 1][j + 1] = '0'


def blocks_fall(m, n, board):
    # 역순으로 리스트 담아서
    blocks = []
    for j in range(n):
        tmp = []
        for i in range(m - 1, -1, -1):
            if board[i][j] != '0':
                tmp.append(board[i][j])
        blocks.append(tmp)
    # transpose 해서 반환하기
    fallen = [[None] * n for _ in range(m)]
    for j in range(n):
        for cur, i in enumerate(range(m - 1, -1, -1)):
            if cur < len(blocks[j]):
                fallen[i][j] = blocks[j][cur]
    return fallen


def solution(m, n, board):
    res = 0
    board = [list(row[:]) for row in board]
    while True:
        color_four_blocks(m, n, board)  # '0' 색칠
        zero_count = sum(row.count('0') for row in board)  # '0' 개수 세서 update
        if zero_count == 0:
            break
        res += zero_count
        board = blocks_fall(m, n, board)  # 블록 떨어지기
        print(board)

    return res


print(solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]))
