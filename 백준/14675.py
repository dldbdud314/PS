'''
14675. 단절점과 단절선
'''
import sys
input = sys.stdin.readline

from collections import defaultdict

n = int(input())
graph = defaultdict(list)
for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

q = int(input())
for _ in range(q):
    t, k = map(int, input().split())
    if t == 2: # 단절선
        print("yes")
    elif t == 1: # 단절점
        if len(graph[k]) < 2:
            print("no")
        else:
            print("yes")