"""
1504. 특정한 최단 경로

** 플로이드 워셜 : 모든 경우의 수에 대해 구하기 -> 시간초과 !!

from itertools import permutations
import sys

input = sys.stdin.readline
INF = 1e18

n, e = map(int, input().split())

graph = [[INF] * (n + 1) for _ in range(n + 1)]
for x in range(1, n + 1):
    graph[x][x] = 0  # 자기자신

for _ in range(e):  # 비용 저장
    a, b, c = map(int, input().split())
    graph[a][b] = c
    graph[b][a] = c

# F-W
for k in range(1, n + 1):
    for a, b in permutations([i for i in range(1, n + 1) if i != k], 2):
        if a == b:
            continue
        graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
        graph[b][a] = min(graph[b][a], graph[b][k] + graph[k][a])

v1, v2 = map(int, input().split())

route1 = graph[1][v1] + graph[v1][v2] + graph[v2][n]
route2 = graph[1][v2] + graph[v2][v1] + graph[v1][n]
route3 = graph[1][v1] + graph[v1][1] + graph[1][v2] + graph[v2][n]
route4 = graph[1][v2] + graph[v2][1] + graph[1][v1] + graph[v1][n]
route5 = graph[1][v1] + graph[v1][1] + graph[1][v2] + graph[v2][1] + graph[1][n]

min_route = min(route1, route2, route3, route4, route5)
print(-1) if min_route == INF else print(min_route)
"""
