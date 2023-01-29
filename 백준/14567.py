"""
선수 과목 (Prerequisite) : topological sort + BFS
"""
from collections import deque
import sys
input = sys.stdin.readline


# 위상 정렬 수행
def topological_sort():
    graph = {i: {'in': 0, 'dest': []} for i in range(1, n + 1)}
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a]['dest'].append(b)
        graph[b]['in'] += 1

    return graph


def find_roots(graph):  # 루트 노드 -> incoming == 0
    res = []
    for k in graph.keys():
        if graph[k]['in'] == 0:
            res.append(k)
    return res


def bfs_traverse(graph):
    levels = [0] * (n + 1)  # 레벨 기록
    roots = find_roots(graph)  # 시작점
    queue = deque(roots)  # 노드들, 레벨 정보
    for root in roots:
        levels[root] = 1
    while queue:
        node = queue.popleft()

        for nxt in graph[node]['dest']:
            graph[nxt]['in'] -= 1
            levels[nxt] = levels[node] + 1  # 레벨 정보 업데이트
            if graph[nxt]['in'] == 0:  # 루트가 되면 다음 방문 노드로 추가하기
                queue.append(nxt)

    return levels


n, m = map(int, input().split())
graph = topological_sort()  # 그래프 만들기
res = bfs_traverse(graph)  # BFS level 별로 접근하며 노드 순회하기 -> 레벨 정보 갱신
print(*res[1:], end=' ')
