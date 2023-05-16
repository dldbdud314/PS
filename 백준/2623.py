"""
2623. 음악 프로그램
** topological sort
"""
import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
incoming = [0] * (n + 1)  # 진입차수
dest = [[] for _ in range(n + 1)]  # 그래프
for _ in range(m):
    links = list(map(int, input().split()))[1:]
    for i in range(len(links)):
        if i > 0:
            incoming[links[i]] += 1
        if i < len(links) - 1:
            dest[links[i]].append(links[i + 1])

queue = deque()
# source 찾아서 enqueue
for node in range(1, n + 1):
    if incoming[node] == 0:
        queue.append(node)

path = []
# t-s
while queue:
    cur = queue.popleft()
    path.append(cur)

    for nxt in dest[cur]:
        if nxt in path: continue  # 사이클 방지
        incoming[nxt] -= 1
        if incoming[nxt] == 0:
            queue.append(nxt)

if len(path) < n:
    print(0)
else:
    print(*path, sep='\n')
