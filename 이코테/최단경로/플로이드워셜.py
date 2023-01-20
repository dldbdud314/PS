'''
플로이드-워셜 base code
=====
input:
4 7
1 2 4
1 4 6
2 1 3
2 3 7
3 1 5
3 4 4
4 3 2
expected output:
0 4 8 6
3 0 7 9
5 9 0 4
7 11 2 0
'''
from itertools import permutations

INF = int(1e9)

n, m = map(int, input().split())  # 노드, 간선 개수
graph = [[INF] * (n + 1) for _ in range(n + 1)]  # dp 그래프

# 자기자신 초기화
for i in range(1, n + 1):
    graph[i][i] = 0

# 연결 정보 입력 받아서 graph 설정
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = c

# 경유지 k에 대해 최단거리 a -> b DP 업데이트
for k in range(1, n + 1):
    for a, b in permutations([i for i in range(1, n + 1) if i != k], 2):
        if a == b:
            continue
        graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# print output
for a in range(1, n + 1):
    for b in range(1, n + 1):
        print(graph[a][b], end=" ") if graph[a][b] < INF else print("INF", end=" ")
    print()
