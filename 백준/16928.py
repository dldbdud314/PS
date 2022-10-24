# 뱀과 사다리 게임

from collections import deque

n, m = map(int, input().split())

ladders = dict()
for _ in range(n):
    x, y = map(int, input().split())
    ladders[x] = y

snakes = dict()
for _ in range(m):
    u, v = map(int, input().split())
    snakes[u] = v


queue = deque([(1, 0)])
visited = [False] * 101
visited[1] = True

while queue:
    cur_pos, level = queue.popleft()

    if cur_pos == 100:
        print(level)
        break

    for move in range(1, 7):
        next_pos = cur_pos + move

        if next_pos <= 100:
            if next_pos in ladders:
                next_pos = ladders[next_pos]
            elif next_pos in snakes:
                next_pos = snakes[next_pos]

            if not visited[next_pos]:
                queue.append((next_pos, level + 1))
                visited[next_pos] = True