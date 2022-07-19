#미로탈출
from collections import deque


def solution(n, m, maze):
    queue = deque([(0, 0, 1)]) #x, y, d
    visited = [[False] * m for _ in range(n)]
    visited[0][0] = True
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)] #좌, 하, 우, 상
    while queue:
        x, y, d = queue.popleft()
        if x == n - 1 and y == m - 1:
            return d
        for dx, dy in dirs:
            if 0 <= x + dx < n and 0 <= y + dy < m and not visited[x+dx][y+dy] and maze[x+dx][y+dy] == 1:
                queue.append((x + dx, y + dy, d + 1)) # 레벨별 거리 += 1
                visited[x+dx][y+dy] = True
    return 1

n, m = map(int, input().split())
maze = [list(map(int, input().split())) for _ in range(n)]
print(solution(n, m, maze))