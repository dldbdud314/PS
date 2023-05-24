"""
1717. 집합의 표현
** 기본 Union-find
"""
import sys
sys.setrecursionlimit(10 ** 5)

input = sys.stdin.readline

n, m = map(int, input().split())
parent = [i for i in range(n + 1)]


def find_parent(x):
    if x != parent[x]:
        parent[x] = find_parent(parent[x])
    return parent[x]


def union(x1, x2):
    x1 = find_parent(x1)
    x2 = find_parent(x2)
    if x1 < x2:
        parent[x2] = x1
    else:
        parent[x1] = x2


for _ in range(m):
    cmd, a, b = map(int, input().split())
    if cmd == 0:  # union
        if a == b: continue
        union(a, b)
    else:  # find
        if a == b:
            print("YES")
            continue
        print("YES") if find_parent(a) == find_parent(b) else print("NO")
