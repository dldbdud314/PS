from itertools import permutations
import sys
input = sys.stdin.readline

INF = int(1e9)

n = int(input())  # 도시 개수
m = int(input())  # 버스 개수
graph = [[INF] * (n + 1) for _ in range(n + 1)]  # 최단거리 DP

for x in range(1, n + 1):  # 자기자신까지의 최단거리
    graph[x][x] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = min(graph[a][b], c)  # 여러 개의 노선 중 최단거리로 저장하기

# F-W
for k in range(1, n + 1):
    for a, b in permutations([i for i in range(1, n + 1) if i != k], 2):
        if a == b:
            continue
        graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(graph[i][j], end=' ') if graph[i][j] < INF else print(0, end=' ')
    print()
