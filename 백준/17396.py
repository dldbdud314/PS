"""
17396. 백도어

** 다익스트라 최단 경로
- 0, a = 0인 지점, n-1 포함한 연결 관계에 대해서 최단 경로 구하기
"""
import sys
from heapq import heappop, heappush

input = sys.stdin.readline
INF = sys.maxsize

n, m = map(int, input().split())
A = list(map(int, input().split()))

graph = [[] for _ in range(n)]  # 연결 관계
dis = [INF for _ in range(n)]  # 최단거리

for _ in range(m):  # 그래프 연결
    a, b, t = map(int, input().split())
    # 양방향 연결, 도착지 a == 1이면 미포함
    if A[b] == 0 or b == n - 1:
        graph[a].append((b, t))
    if A[a] == 0 or a == n - 1:
        graph[b].append((a, t))
'''
- me : 애초에 도착지가 0인 경우만 그래프에 포함시켰다
- others : dijkstra 수행하면서 A에 해당하는 도착지는 제외하고 count 하는 방법도 있음
'''


def dijkstra(start):
    queue = []
    heappush(queue, (0, start))
    dis[start] = 0
    while queue:
        ct, cc = heappop(queue)
        if dis[cc] < ct:
            continue
        for b, t in graph[cc]:
            time = ct + t
            if time < dis[b]:
                dis[b] = time
                heappush(queue, (time, b))


dijkstra(0)

print(-1) if dis[n - 1] == INF else print(dis[n - 1])
