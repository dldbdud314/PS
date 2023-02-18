"""
[6443. 애너그램](https://www.acmicpc.net/problem/6443)
** backtracking (DFS) - 풀참
"""
import sys
input = sys.stdin.readline


def dfs(cur_s, v, target, used):
    if len(cur_s) == len(target):  # 종료 조건
        print(cur_s)
        return

    for i in range(len(target)):
        if not v[i]:
            to_add = cur_s + target[i]
            if to_add not in used:
                used.add(to_add)
                v[i] = True
                dfs(to_add, v, target, used)
                v[i] = False


def solution():
    s = ''.join(sorted(list(input().strip())))  # 알파벳 순

    v = [False] * len(s)
    used = set()
    dfs('', v, s, used)  # 현재 단어, 자리별 사용 여부, 원래 단어, 사용한 단어들(백트래킹용)


T = int(input())
for _ in range(T):
    solution()
