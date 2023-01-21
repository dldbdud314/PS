"""
내 풀이: BFS + DP

input:
3
3
5 5 4
3 9 1
3 2 7
5
3 7 2 0 1
2 8 0 9 1
1 2 1 8 1
9 8 9 2 0
3 6 5 1 5
7
9 0 5 1 1 5 3
4 1 2 1 6 5 3
0 7 6 1 6 8 5
1 1 7 8 3 2 3
9 4 0 7 6 4 1
5 8 3 2 4 8 3
7 4 8 4 8 3 4

output:
20
19
36
"""
from collections import deque
INF = int(1e9)
dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def move():
    n = int(input())
    space = [list(map(int, input().split())) for _ in range(n)]
    dp = [[INF] * n for _ in range(n)]  # 최소 비용 저장

    queue = deque([(0, 0, space[0][0])])  # x, y좌표, 현재 비용
    while queue:
        cx, cy, cost = queue.popleft()
        for dx, dy in dirs:
            if 0 <= cx + dx < n and 0 <= cy + dy < n and cost + space[cx + dx][cy + dy] <= dp[cx + dx][cy + dy]:
                dp[cx + dx][cy + dy] = cost + space[cx + dx][cy + dy]
                queue.append((cx + dx, cy + dy, cost + space[cx + dx][cy + dy]))

    return dp[n-1][n-1]


T = int(input())
res = []
for _ in range(T):
    res.append(move())

print(*res, sep='\n')
