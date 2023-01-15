"""
bruteforce + DFS : 각각의 전선(연결관계)를 끊어 보고, 그떄 노드 개수의 차이가 최소인 경우 구하기
"""
from collections import defaultdict


def dfs(tree, cur, visited):
    visited.add(cur)
    for nxt in tree[cur]:
        if nxt not in visited:
            dfs(tree, nxt, visited)

    return len(visited)


# 자른 뒤에 그래프를 만든 뒤, dfs 탐색하며 노드 개수 세기, 차이 계산해서 return
def cut(idx, n, wires):
    tree = defaultdict(list)
    for i in range(len(wires)):
        if i == idx:
            continue
        v1, v2 = wires[i]
        tree[v1].append(v2)
        tree[v2].append(v1)

    visited1, visited2 = set(), set()
    cnt1 = dfs(tree, wires[idx][0], visited1)
    cnt2 = dfs(tree, wires[idx][1], visited2)

    return abs(cnt1 - cnt2)


def solution(n, wires):
    res = float('inf')
    for i in range(len(wires)):  # i는 wires에서 제거할 연결 관계의 인덱스
        res = min(cut(i, n, wires[:]), res)

    return res
