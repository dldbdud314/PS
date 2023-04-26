"""
1043. 거짓말

** DFS
- 진실을 아는 사람들이 속한 그룹 -> infect
- 해당 그룹의 다른 사람들이 속한 그룹 -> infect
"""
import sys
sys.setrecursionlimit(10 ** 5)

n, m = map(int, input().split())

truths = list(map(int, input().split()))[1:]  # 진실을 아는 사람들

parties = []
graph = [[] for _ in range(n + 1)]  # 사람별 참석 파티
for i in range(m):
    ppl = list(map(int, input().split()))[1:]
    parties.append(ppl)
    for x in ppl:
        graph[x].append(i)


def spread(curP):
    for party in graph[curP]:
        if not infected[party]:
            infected[party] = True

            for nxtP in parties[party]:
                if nxtP != curP:
                    spread(nxtP)


infected = [False] * m
for truth in truths:
    spread(truth)

print(infected.count(False))
