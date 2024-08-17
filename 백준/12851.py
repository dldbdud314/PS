# updated: 240817
from collections import deque

n, k = map(int, input().split())
vis = [False] * 100001

queue = deque([(n, 0)])  # 현재 위치, jump
min_jump = float('inf')
jcnt = 0
while queue:
    x, cnt = queue.popleft()
    vis[x] = True

    if min_jump < cnt:
        break
    if x == k:
        min_jump = cnt
        jcnt += 1

    for nxt in [x - 1, x + 1, 2 * x]:
        if 0 <= nxt < 100001 and not vis[nxt]:
            queue.append((nxt, cnt + 1))

print(min_jump)
print(jcnt)