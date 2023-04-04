"""
1325. 효율적인 해킹 - FAIL !

** DFS
단순 dfs로는 시간 초과 ,,
 - 사이클 고려 필요 -> 그렇게 되면 visited 쓸 이유가,,
 - 사이클 여부 확인하고, 해당 노드들에 대해 전부 res에 추가할 것 ..

++
Python dfs는 시간 초과, PyPy로 해보니 메모리 초과 ,,
다른 풀이 보니 다들 bfs + PyPy로 통과 시킴 .. 사이클 여부에 따른 visited 처리 모르겠다 !!!! x_x
"""
import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline


def dfs(root, cur, cur_nodes):
    global is_cycle
    cur_nodes.add(cur)

    for nxt in graph[cur]:
        if nxt == root:  # 사이클 존재
            is_cycle = True
        if nxt not in cur_nodes:
            dfs(root, nxt, cur_nodes)

    return len(cur_nodes)


n, m = map(int, input().split())
graph = [list() for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[b].append(a)

max_nodes = 0

# dfs
res = []
cycles = set()  # 사이클 존재하는 노드 제외하고 한번씩 돌기 .. ?!
for node in range(1, n + 1):
    if node not in cycles:
        is_cycle = False  # 시작 노드와 만나는 경우, 사이클 존재
        nodes = set()  # 사이클 있으면 전부 res 추가 대상
        cnt = dfs(node, node, nodes)  # root 노드, 현재 노드, 노드 sets
        # print(node, is_cycle, nodes)
        if max_nodes < cnt:
            max_nodes = cnt
            res = []  # clear -> O(n)..?
            if is_cycle:
                res.extend(list(nodes))
                cycles.update(nodes)
            else:
                res.append(node)
        elif max_nodes == cnt:
            res.append(node)

print(*res, sep=' ')
