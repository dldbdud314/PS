"""
1238. 파티

** 다익스트라 : k -> x -> k 최단 경로가 가장 긴 사람 구하기, 2번의 다익스트라 수행
- 두가지 버전의 그래프 만들기
- 출발할 때 : k -> x reverse dijkstra
- 돌아갈 때 : x -> k forward dijkstra
"""
from heapq import heappop, heappush
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m, x = map(int, input().split())

forward = [[] for _ in range(n + 1)]
backward = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, t = map(int, input().split())
    forward[a].append((b, t))
    backward[b].append((a, t))

# 목적지 x에서 각각의 점까지 최단거리
dist_f, dist_b = [INF] * (n + 1), [INF] * (n + 1)


def dijkstra_reverse(start):
    queue = []
    heappush(queue, (0, start))
    dist_b[start] = 0
    while queue:
        d, k = heappop(queue)
        if dist_b[k] < d:
            continue
        for b, c in backward[k]:
            nd = d + c
            if nd < dist_b[b]:
                dist_b[b] = nd
                heappush(queue, (nd, b))


def dijkstra(start):
    queue = []
    heappush(queue, (0, start))
    dist_f[start] = 0
    while queue:
        d, k = heappop(queue)
        if dist_f[k] < d:
            continue
        for b, c in forward[k]:
            nd = d + c
            if nd < dist_f[b]:
                dist_f[b] = nd
                heappush(queue, (nd, b))


# 출발지에서 목적지까지 -> 역방향 다익스트라
dijkstra_reverse(x)

# 목적지에서 출발지까지 -> 정방향 다익스트라
dijkstra(x)


maxDist = 0
for d1, d2 in zip(dist_b[1:], dist_f[1:]):
    maxDist = max(maxDist, d1 + d2)

print(maxDist)
