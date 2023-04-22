"""
** 최소신장트리 만들기 (Kruskal)
"""
import sys
input = sys.stdin.readline


def find_parent(p, x):
    if p[x] != x:
        p[x] = find_parent(p, p[x])
    return p[x]


def union_parent(p, x1, x2):
    x1 = find_parent(parent, x1)
    x2 = find_parent(parent, x2)
    if x1 < x2:
        p[x2] = x1
    else:
        p[x1] = x2


n, m = map(int, input().split())
# 노드값 1 ~ n
parent = [i for i in range(n + 1)]

edges = []
for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))

edges.sort()  # 간선 정렬

last = 0
total = 0
for c, a, b in edges:
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        total += c
        last = c

print(total - last)
