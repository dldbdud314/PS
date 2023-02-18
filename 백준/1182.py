"""
[1182. 부분 수열의 합](https://www.acmicpc.net/problem/1182)
** 백트래킹 - 풀참
- 포함 하는 경우/아닌 경우 니눠서 생각 !
"""
import sys

input = sys.stdin.readline


def dfs(cur_sum, depth, arr):
    if depth >= len(arr):
        return

    cur_sum += arr[depth]

    if cur_sum == s:
        global count
        count += 1

    dfs(cur_sum, depth + 1, arr)  # 선택한 경우
    dfs(cur_sum - arr[depth], depth + 1, arr)  # 선택 하지 않은 경우


count = 0

n, s = map(int, input().split())
lst = list(map(int, input().split()))

dfs(0, 0, lst)

print(count)

"""
SOL 2)
** BFS, 같은 아이디어에서 출발 -> 메모리 초과로 실패 !
"""
from collections import deque


def bfs():
    queue = deque([0])

    for i in range(len(lst)):
        num = lst[i]
        for _ in range(2 ** n):
            cur = queue.popleft()
            queue.append(cur)
            queue.append(cur + num)

    return queue.count(s)


print(bfs())
