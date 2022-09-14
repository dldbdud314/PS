#최단경로
from heapq import heappop, heappush
import sys
input = sys.stdin.readline
INF = int(1e9)

def solution(start, graph, distance):
    queue = []
    heappush(queue, (0, start))
    distance[start] = 0
    while queue:
        dist, now = heappop(queue)
        if distance[now] < dist:
            continue
        for b, c in graph[now]:
            cost = dist + c
            if cost < distance[b]:
                distance[b] = cost
                heappush(queue, (cost, b))
            
v, e = map(int, input().split())
start = int(input())
graph = [[] for _ in range(v + 1)]
distance = [INF] * (v + 1)
for _ in range(e):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
solution(start, graph, distance)
distance.remove(INF) #첫번쨰 원소 삭제
for k in distance:
    print("INF" if k == INF else k)