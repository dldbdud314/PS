#문제집
import sys
input = sys.stdin.readline

from heapq import heappop, heappush

def topological_sort(n, info):
    graph = {i + 1 : {'incoming' : 0, 'dest' : []} for i in range(n)}
    for a, b in info:
        graph[a]['dest'].append(b)
        graph[b]['incoming'] += 1
    for k in graph.keys(): #목적지 sort
        graph[k]['dest'].sort()
    return graph

def solution(n, info):
    graph = topological_sort(n, info)
    heap = [] #min heap에 source 넣고 시작
    for k in graph.keys():
        if graph[k]['incoming'] == 0:
            heappush(heap, k)
    res = [] # BFS - heap 활용
    while heap:
        cur = heappop(heap)
        res.append(cur)
        for next in graph[cur]['dest']:
            graph[next]['incoming'] -= 1
            if graph[next]['incoming'] == 0:
                heappush(heap, next)
    return res

n, m = map(int, input().split())
info = []
for _ in range(m):
    info.append(map(int, input().split()))
res = solution(n, info)
for x in res:
    print(x, end = ' ')