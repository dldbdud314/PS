"""
15649. N과 M (1)
** backtracking으로 중복 없이 순열 구현
"""


def dfs(num, lst):
    if len(lst) == m:
        print(*lst)
        return

    for k in range(1, n + 1):
        if not used[k] and k not in lst:
            used[k] = True
            dfs(k, lst + [k])
            used[k] = False


n, m = map(int, input().split())
used = [False] * (n + 1)
dfs(0, [])
