"""
15652. N과 M (4)
** backtracking으로 중복 허용, 비내림차순 순열 구현
"""


def dfs(num, lst):
    if len(lst) == m:
        print(*lst)
        return

    for k in range(1, n + 1):
        if not lst or k >= lst[-1]:
            dfs(k, lst + [k])


n, m = map(int, input().split())
dfs(0, [])
