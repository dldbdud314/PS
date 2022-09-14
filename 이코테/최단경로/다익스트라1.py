import sys
input = sys.stdin.readline
INF = int(1e9)

#입력 & 초기화
n, m = map(int, input().split()) #노드, 간선 개수
start = int(input())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
distance = [INF] * (n + 1)
for _ in range(m): #간선 정보
    a, b, c = map(int, input().split()) #a -> b, 비용: c
    graph[a].append((b, c))
#print(graph) #그래프 정보

def get_smallest_node():
    min_value = INF
    idx = 0
    for i in range(1, n + 1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            idx = i
    return idx

def dijkstra(start):
    #시작 노드 초기화
    distance[start] = 0
    visited[start] = True
    for b, c in graph[start]:
        distance[b] = c
    for _ in range(n - 1):
        now = get_smallest_node()
        visited[now] = True
        for b, c in graph[now]:
            cost = distance[now] + c
            if cost < distance[b]:
                distance[b] = cost
        
dijkstra(start)

#최단거리 출력
for i in range(1, n + 1):
    print('INFINITY' if distance[i] == INF else distance[i], end = ' ')