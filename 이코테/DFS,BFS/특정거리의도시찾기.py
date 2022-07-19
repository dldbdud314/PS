#백준 18352번
import sys
from collections import deque

def solution(n, k, x, graph):
    visited = [False] * (n + 1)
    queue = deque([(x, 0)])
    visited[x] = True
    ans = []
    while queue:
        node, d = queue.popleft()
        if d == k: 
            ans.append(node)
        elif d > k: 
            break
        for next in graph[node]:
            if not visited[next]:
                queue.append((next, d + 1))
                visited[next] = True
    return sorted(ans)

def make_graph(n, links):
    graph = {k : list() for k in range(1, n + 1)}
    for a, b in links:
        graph[a].append(b)
    return graph

n, m, k, x = map(int, input().split())
links = []
for _ in range(m):
    links.append(list(map(int, sys.stdin.readline().split())))
graph = make_graph(n, links) #인접 리스트 형태로 만들기
res = solution(n, k, x, graph)
if not res:
    print(-1)
else:
    for x in res: print(x)