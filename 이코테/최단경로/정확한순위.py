"""
F-W
K의 순위를 정확히 알 수 있다는 건?
- (X -> K 개수) + (K -> Y  개수) == n - 1 (다른 노드들은 모두 K와의 연결 관계가 있음)

input:
6 6
1 5
3 4
4 2
4 6
5 2
5 4

output:
1
"""
from itertools import permutations
import sys
input = sys.stdin.readline

INF = int(1e9)

n, m = map(int, input().split())
graph = [[INF] * (n + 1) for _ in range(n + 1)]

for x in range(1, n + 1):
    graph[x][x] = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1

for k in range(1, n + 1):
    for a, b in permutations([i for i in range(1, n + 1) if i != k], 2):
        if a == b:
            continue
        graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

cnt = 0
for k in range(1, n + 1):
    linked = 0
    for l in range(1, n + 1):
        if k == l:
            continue
        if graph[l][k] < INF or graph[k][l] < INF:
            linked += 1
    if linked == n - 1:
        cnt += 1

print(cnt)