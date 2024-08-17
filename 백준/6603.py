'''
6603. 로또
** backtracking, dfs
'''
import sys

input = sys.stdin.readline


def dfs(idx, cur_lst):
    if len(cur_lst) == 6:
        print(*cur_lst, end='\n')
        return

    for i in range(idx, k):
        if not used[i]:
            used[i] = True
            dfs(i, cur_lst + [nums[i]])
            used[i] = False


while True:
    k, *nums = map(int, input().split())
    if k == 0: break

    used = [False] * k
    dfs(0, [])
    print()