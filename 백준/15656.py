"""
15656. N과 M (7)
** backtracking 순열, 주어진 리스트, 중복 허용 사전순
"""


def dfs(idx, cur_arr):
    if len(cur_arr) == m:
        print(*cur_arr)
        return

    for i in range(n):
        dfs(i, cur_arr + [arr[i]])


n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

dfs(0, [])
