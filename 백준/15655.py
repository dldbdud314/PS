"""
15655. N과 M (6)
** backtracking 순열, 주어진 리스트, 오름차순
"""


def dfs(idx, cur_arr):
    if len(cur_arr) == m:
        print(*cur_arr)
        return

    for i in range(idx, n):
        if not cur_arr or arr[i] > cur_arr[-1]:
            dfs(i, cur_arr + [arr[i]])


n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

dfs(0, [])
