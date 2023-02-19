"""
15666. N과 M (12)
** backtracking - 원소 중복 허용, 순열 중복 허용 X, 비내림차순
"""


def dfs(idx, cur_arr):
    if len(cur_arr) == m:
        if tuple(cur_arr) not in v:
            v.add(tuple(cur_arr))
            print(*cur_arr)
        return

    for i in range(idx, n):
        dfs(i, cur_arr + [arr[i]])


n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

v = set()
dfs(0, [])
