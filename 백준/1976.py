"""
1976. 여행 가자

sol 1
** 플로이드 워셜
- 최단거리를 구하는 문제는 아니지만 모든 노드 -> 다른 노드 연결 관계 알 수 있다는 점 이용
- a -> b 직간접적인 연결 관계만 입증 되면 YES !
- M ~> 1000 이므로 연결 관계 캐싱 해서 활용하는 게 효율적 !
"""
from itertools import permutations
import sys
input = sys.stdin.readline

INF = 1e9

n = int(input())
m = int(input())
adj_matrix = [list(map(int, input().split())) for _ in range(n)]

graph = [[INF] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i == j:
            graph[i][j] = 0  # 자기자신
        elif adj_matrix[i][j] == 1:
            graph[i][j] = 1  # 직접적인 연결

# F-W
for k in range(n):
    for a, b in permutations([i for i in range(n) if i != k], 2):
        if a == b:
            continue
        graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

links = list(map(int, input().split()))  # 여행 계획

success = True
for i in range(1, m):
    a, b = links[i - 1] - 1, links[i] - 1
    if graph[a][b] == INF:
        success = False
        break

print("YES" if success else "NO")

"""
sol 2
** Union-Find
- 인접 행렬 이용해서 union
- 여행 계획 순회하면서 find
"""
import sys
input = sys.stdin.readline


def find_parent(p, x):
    if p[x] != x:
        p[x] = find_parent(p, p[x])
    return p[x]


def union_parent(p, a, b):
    a = find_parent(p, a)
    b = find_parent(p, b)

    if a < b:
        p[b] = a
    else:
        p[a] = b


n = int(input())
m = int(input())
adj_matrix = [list(map(int, input().split())) for _ in range(n)]

parent = [i for i in range(n)]

for i in range(n):
    for j in range(i, n):
        if adj_matrix[i][j] == 1:
            union_parent(parent, i, j)

links = list(map(int, input().split()))  # 여행 계획

success = True
for i in range(1, m):
    a, b = links[i - 1] - 1, links[i] - 1
    if find_parent(parent, a) != find_parent(parent, b):
        success = False
        break

print("YES") if success else print("NO")
