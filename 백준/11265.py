'''
11265. 끝나지 않는 파티
** 플로이드-워셜 : 모든 노드에 대해 최단 거리 구하기
'''
from itertools import permutations
import sys
input = sys.stdin.readline


n, m = map(int, input().split())  # 도시 개수, 쿼리 개수
graph = [list(map(int, input().split())) for _ in range(n)]  # 파티장 간의 연결 정보

# F - W
for k in range(n):
    for a, b in permutations([i for i in range(n) if i != k], 2):
        if a == b:
            continue
        if graph[a][b] > graph[a][k] + graph[k][b]:  # 시간 초과 수정 -> min 활용시 불필요한 할당 작업 늘어난다
            graph[a][b] = graph[a][k] + graph[k][b]

res = []  # true, false
for _ in range(m):
    a, b, c = map(int, input().split())
    if graph[a - 1][b - 1] <= c:
        res.append(True)
    else:
        res.append(False)

for i in range(len(res)):
    print("Enjoy other party") if res[i] else print("Stay here")
