"""
1342. 행운의 문자열
** 백트래킹 DFS (순열, 단 결과의 중복 없이)
"""
import sys
sys.setrecursionlimit(10 ** 6)


def dfs(cur):
    if len(cur) == len(S):
        global res
        res.add(cur)
        return

    for i in range(len(S)):
        if not visited[i] and (not cur or cur[-1] != S[i]):
            visited[i] = True
            dfs(cur + S[i])
            visited[i] = False


S = input()
visited = [False] * len(S)

res = set()
dfs('')
print(len(res))
