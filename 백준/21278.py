#호석이두마리치킨
from collections import defaultdict, deque
from itertools import combinations

n, m = map(int, input().split())
graph = defaultdict(list)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
#a - b 최단거리 미리 구해놓기 (BFS 활용)
lengths = [[0] * (n + 1) for _ in range(n + 1)]
for s, t in combinations(list(range(1, n + 1)), 2):
    queue = deque([(s, 0)])
    visited = [False] * (n + 1)
    while queue:
        cur, l = queue.popleft()
        visited[cur] = True
        if cur == t:
            lengths[s][t] = l #양방향으로 거리 정보 추가
            lengths[t][s] = l
            break
        for next in graph[cur]:
            if not visited[next]: 
                queue.append((next, l + 1))

shortest_sum = float('inf')
p1, p2 = 0, 0
for t1, t2 in combinations(list(range(1, n + 1)), 2):
    total = 0
    for s in range(1, n + 1): #각각의 집별로 최단거리 계산
        if s != t1 and s != t2:
            total += min(lengths[s][t1], lengths[s][t2]) * 2
    if shortest_sum > total:
        shortest_sum = total
        p1, p2 = t1, t2

print(p1, p2, shortest_sum, sep = ' ')