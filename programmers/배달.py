from heapq import heappush, heappop
INF = int(1e9)

def dijkstra(start, distance, graph):
    queue = []
    heappush(queue, (0, start))
    distance[start] = 0
    while queue:
        dist, now = heappop(queue)
        if distance[now] < dist:
            continue
        for b, c in graph[now]:
            cost = distance[now] + c
            if cost < distance[b]:
                distance[b] = cost
                heappush(queue, (cost, b))

def solution(N, road, K):
    distance = [INF] * (N + 1)
    start = 1
    graph = [[] for _ in range(N + 1)]
    for a, b, c in road: #양방향 그래프 처리?
        graph[a].append((b, c))
        graph[b].append((a, c))
    dijkstra(start, distance, graph)
    cnt = 0
    for i in range(1, N + 1):
        if distance[i] <= K:
            cnt += 1
    return cnt

print(solution(6, [[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]], 4))