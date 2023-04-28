"""
16562. 친구비
** union-find
"""
import sys
input = sys.stdin.readline

INF = sys.maxsize

n, m, k = map(int, input().split())
parent = [i for i in range(n + 1)]


def find_parent(p, x):
    if p[x] != x:
        p[x] = find_parent(p, p[x])

    return p[x]


def union_parent(p, x1, x2):
    x1 = find_parent(p, x1)
    x2 = find_parent(p, x2)
    if x1 < x2:
        p[x2] = x1
    else:
        p[x1] = x2


pays = [0] + list(map(int, input().split()))

for _ in range(m):
    a, b = map(int, input().split())
    union_parent(parent, a, b)

min_pays = dict()
for i in range(1, n + 1):
    group = find_parent(parent, i)
    if (group in min_pays and pays[i] < min_pays[group]) or group not in min_pays:
        min_pays[group] = pays[i]

total = sum(min_pays.values())
print("Oh no ") if total > k else print(total)
