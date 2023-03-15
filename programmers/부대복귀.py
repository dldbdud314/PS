"""
** BFS 최단 거리
- destination -> 다른 모든 노드(sources)까지 최단 경로 구하기
"""
from collections import deque


def solution(n, roads, sources, destination):
    # 거리 정보 그래프
    graph = [[] for _ in range(n + 1)]
    for a, b in roads:
        graph[a].append(b)
        graph[b].append(a)

    dists = [-1] * (n + 1)  # 최단 경로 (도달X -> -1)

    # bfs 한번 -> 다른 모든 노드까지 최단 경로 갱신하기
    queue = deque([destination])
    dists[destination] = 0
    while queue:
        cur = queue.popleft()
        for nxt in graph[cur]:
            if dists[nxt] == -1:
                queue.append(nxt)
                dists[nxt] = dists[cur] + 1

    return [dists[source] for source in sources]
