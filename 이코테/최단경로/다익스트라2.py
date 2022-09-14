#개선된 시간 복잡도 -> O(ElogV)
from heapq import heappop, heappush
import sys
input = sys.stdin.readline
INF = int(1e9)

#입력 & 초기화
n, m = map(int, input().split()) #노드, 간선 개수
start = int(input())
graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)
for _ in range(m): #간선 정보
    a, b, c = map(int, input().split()) #a -> b, 비용: c
    graph[a].append((b, c))
    
def dijkstra(start):
    queue = []
    heappush(queue, (0, start))
    distance[start] = 0
    while queue:
        dist , now = heappop(queue)
        if distance[now] < dist:
            continue
        for b, c in graph[now]:
            cost = dist + c
            if cost < distance[b]:
                distance[b] = cost
                heappush(queue, (cost, b))

dijkstra(start)

#최단거리 출력
for i in range(1, n + 1):
    print('INFINITY' if distance[i] == INF else distance[i], end = ' ')    