# 플로이드 워셜

from itertools import permutations
INF = int(1e9)

n, m = map(int, input().split())  # 회사, 연결 개수
graph = [[INF] * (n + 1) for _ in range(n + 1)]  # 최단거리 dp

for i in range(1, n + 1):
    graph[i][i] = 0  # row == col -> 거리 0으로 설정

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1  # 양방향 연결
    graph[b][a] = 1

x, k = map(int, input().split())  # 회사, 소개팅 장소

# F-W 수행
for i in range(1, n + 1):
    for a, b in permutations([j for j in range(1, n + 1) if j != i], 2):
        if a == b:
            continue
        graph[a][b] = min(graph[a][b], graph[a][i] + graph[i][b])

# output
print(graph[1][k] + graph[k][x]) if (graph[1][k] < INF and graph[k][x] < INF) else print(-1)
