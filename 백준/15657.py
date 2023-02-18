"""
15657. N과 M (8)
** backtracking - 순열, 중복 허용, 비내림차순
"""


def dfs(idx, cur_arr):
    if len(cur_arr) == m:
        print(*cur_arr)
        return

    for i in range(idx, n):
        dfs(i, cur_arr + [arr[i]])


n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

dfs(0, [])
