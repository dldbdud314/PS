"""
** 최소한의 비용으로 구성되는 신장 트리(= MST, Minimum Spanning Tree) -> 그리디

- 간선 데이터를 비용에 따라 오름차순 정렬
- 간선을 확인하며 사이클이 발생하지 않는 경우, MST에 포함
"""


def find_parent(p, x):
    if p[x] != x:
        p[x] = find_parent(p, p[x])
    return p[x]


# 합치기
def union_parent(p, x1, x2):
    x1 = find_parent(p, x1)
    x2 = find_parent(p, x2)
    if x1 < x2:  # 번호가 더 작은 쪽을 부모로 설정하기
        p[x2] = x1
    else:
        p[x1] = x2


v, e = map(int, input().split())
parent = [i for i in range(v + 1)]  # 자기자신을 부모로 초기화

# 간선 정보 입력, 비용에 따라 오름차순 정렬
edges = []
for _ in range(e):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

edges.sort()

# kruskal 수행
total_cost = 0
for c, a, b in edges:
    p1 = find_parent(parent, a)
    p2 = find_parent(parent, b)

    if p1 != p2:  # 사이클이 없는 경우, MST 포함
        union_parent(parent, p1, p2)
        total_cost += c

print(total_cost)
