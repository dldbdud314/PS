# 달이 차오른다, 가자
from collections import deque


def find_minsik(n, m, maze):
    for i in range(n):
        for j in range(m):
            if maze[i][j] == '0':
                return [i, j]


# 키를 다시 가지러 가는 경우는 통행 가넝해야 하는디,, visited 우야노,,
# 아 비트마스크 알아야 함,,!!
def solution(n, m, maze):
    mx, my = find_minsik(n, m, maze)
    queue = deque([(mx, my, set(), 0)])
    visited = [[False] * m for _ in range(n)]
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    while queue:
        x, y, keys, d = queue.popleft()
        print(x, y, keys, d)
        if maze[x][y] == '1':
            return d
        visited[x][y] = True
        for dx, dy in dirs:
            if 0 <= x + dx < n and 0 <= y + dy < m and not visited[x+dx][y+dy] and maze[x+dx][y+dy] != '#':
                if 'A' <= maze[x+dx][y+dy] <= 'F' and maze[x+dx][y+dy].lower() not in keys:
                    continue
                if 'a' <= maze[x+dx][y+dy] <= 'f':
                    keys.add(maze[x+dx][y+dy])
                queue.append((x + dx, y + dy, keys, d + 1))
    return -1


n, m = map(int, input().split())
maze = []
for _ in range(n):
    maze.append(input())
print(solution(n, m, maze))