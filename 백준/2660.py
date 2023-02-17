'''
2660. 회장 뽑기
** 플로이드-워셜 : 자기자신에서 다른 모든 사람까지의 최단거리를 알아야 하기 때문
'''
from itertools import combinations

INF = int(1e9)

n = int(input())
graph = [[INF] * (n + 1) for _ in range(n + 1)]  # 친구 관계 그래프
for x in range(1, n + 1):  # 자기 자신은 0으로
    graph[x][x] = 0
while True:
    a, b = map(int, input().split())
    if a == -1 and b == -1:
        break
    graph[a][b] = 1
    graph[b][a] = 1

# F - W
for k in range(1, n + 1):
    for a, b in combinations([i for i in range(1, n + 1) if i != k], 2):  # combinations -> 양방향 한번에 갱신
        if a == b:
            continue
        graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
        graph[b][a] = min(graph[b][a], graph[b][k] + graph[k][a])

# 사람별 점수 계산
scores = [INF, ]  # 0번째 인덱스
for k in range(1, n + 1):
    scores.append(max(graph[k][1:]))

min_score = min(scores)  # 최소 점수 => 회장 후보
candidates = []  # 회장 후보
for i in range(1, n + 1):
    if scores[i] == min_score:
        candidates.append(i)

print(min_score, len(candidates))
print(*candidates)
