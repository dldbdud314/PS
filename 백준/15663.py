"""
15663. N과 M (9)
** backtracking - 순열, 중복 수열 X
"""


def dfs(idx, cur_arr):
    if len(cur_arr) == m:
        if tuple(cur_arr) not in v:
            v.add(tuple(cur_arr))
            print(*cur_arr)
        return

    for i in range(n):
        if not used[i]:
            used[i] = True
            dfs(i, cur_arr + [arr[i]])
            used[i] = False


n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

used = [False] * n
v = set()
dfs(0, [])
