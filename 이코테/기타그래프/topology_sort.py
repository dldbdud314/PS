"""
위상정렬 베이스 코드
"""
from collections import deque

# input
v, e = map(int, input().split())
indegree = [0] * (v + 1)
graph = [[] for _ in range(v + 1)]
for _ in range(e):
    a, b = map(int, input().split())
    indegree[b] += 1
    graph[a].append(b)

res = []

# topological sort
queue = deque([])  # 진입 차수 == 0인 노드만 가진 큐
for i in range(1, v + 1):
    if indegree[i] == 0:
        queue.append(i)

while queue:
    cur = queue.popleft()
    res.append(cur)

    for nxt in graph[cur]:
        indegree[nxt] -= 1
        if indegree[nxt] == 0:
            queue.append(nxt)

print(*res)
