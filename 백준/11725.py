'''
11725. 트리의 부모 찾기
- bfs로 현재 노드(부모) -> 다음 노드(자식) 순회하면서 부모 노드 업데이트
'''
import sys

input = sys.stdin.readline

from collections import deque, defaultdict

n = int(input())

graph = defaultdict(set)
for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].add(b)
    graph[b].add(a)

p_node = [0] * (n + 1)  # 부모 노드 기록
queue = deque([1])
p_node[1] = 1
while queue:
    cur = queue.popleft()
    for nxt in graph[cur]:
        if p_node[nxt] == 0:
            queue.append(nxt)
            p_node[nxt] = cur

for i in range(2, n + 1):
    print(p_node[i])