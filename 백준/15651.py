"""
15651. N과 M (3)
** backtracking으로 중복 허용, 순열 구현
"""


def dfs(num, lst):
    if len(lst) == m:
        print(*lst)
        return

    for k in range(1, n + 1):  # 중복 허용 -> used 체크 안해도 .. !
        dfs(k, lst + [k])


n, m = map(int, input().split())
dfs(0, [])
