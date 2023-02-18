"""
15654. N과 M (5)
** backtracking 순열, 주어진 리스트
"""


def dfs(idx, cur_arr):
    if len(cur_arr) == m:
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
dfs(0, [])
