"""
** union-find
"""


def find_parent(p, x):
    if p[x] != x:
        p[x] = find_parent(p, p[x])
    return p[x]


def union_parent(p, a, b):
    p1 = find_parent(p, a)
    p2 = find_parent(p, b)

    if p1 < p2:
        p[b] = p1
    else:
        p[a] = p2


n, m = map(int, input().split())
parent = [i for i in range(n + 1)]  # 부모 테이블

for _ in range(m):
    cmd, a, b = map(int, input().split())

    if cmd == 0:
        union_parent(parent, a, b)
    else:
        print("YES") if find_parent(parent, a) == find_parent(parent, b) else print("NO")
