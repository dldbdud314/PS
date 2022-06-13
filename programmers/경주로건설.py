#dfs로 가능한 모든 경로 기록하고 그 중 최소 비용의 경로를 return 한다.
#시간 초과 : 52.0 / 100.0
paths = []

def dfs_paths(board, s, e, visited):
    visited = visited + [s]
    if s == e:
        paths.append(visited)
        return
    dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    for dx, dy in dirs:
        if 0 <= s[0] + dx < len(board) and 0 <= s[1] + dy < len(board) and board[s[0]+dx][s[1]+dy]==0 and [s[0]+dx, s[1]+dy] not in visited:
            dfs_paths(board, [s[0]+dx, s[1]+dy], e, visited)

def calculate_path(path):
    val = 0
    for i in range(len(path)):
        cur_x, cur_y = path[i][0], path[i][1]
        if 0 < i < len(path)-1:
            #corner인 경우:
            # - 이전 x좌표 != 현재 x좌표 && 현재 y좌표 != 다음 y좌표
            # - 이전 y좌표 != 현재 y좌표 && 현재 x좌표 != 다음 x좌표
            last_x, last_y = path[i-1][0], path[i-1][1]
            next_x, next_y = path[i+1][0], path[i+1][1]
            if (last_x != cur_x and cur_y != next_y) or (last_y != cur_y and cur_x != next_x):
                val += 500
            val += 100
    return val + 100

def solution(board):
    s = [0, 0]
    e = [len(board)-1, len(board)-1]
    visited = []
    dfs_paths(board, s, e, visited)
    path_val = []
    for path in paths:
        path_val.append(calculate_path(path))
    return min(path_val)

print(solution([[0,0,0,0,0,0],[0,1,1,1,1,0],[0,0,1,0,0,0],[1,0,0,1,0,1],[0,1,0,0,0,1],[0,0,0,0,0,0]]))
