"""
1535. 안녕
"""
n = int(input())
l = list(map(int, input().split()))  # 체력
j = list(map(int, input().split()))  # 기쁨

"""
** DP
- bottom-up 도전 ,,
    - dp[i] 돌면서 현재 체력에 대해 먹을 수 있는가 ? 있다면 기쁨 갱신 .. !!
- dp[idx][현재 체력]
"""
dp = [[-1] * 101 for _ in range(n + 1)]  # 현재 해당 체력에서의 최대 기쁨 0 ~ 100
dp[0][100] = 0  # default : 체력 100, 기쁨 0

# bottom-up
for i in range(n):
    for k in range(1, 101):
        if dp[i][k] > -1:
            if k - l[i] > 0:  # 인사 한 경우, 안 한 경우 모두 반영
                dp[i + 1][k] = max(dp[i][k], dp[i + 1][k])
                dp[i + 1][k - l[i]] = max(dp[i][k] + j[i], dp[i + 1][k - l[i]])
            else:
                dp[i + 1][k] = max(dp[i][k], dp[i + 1][k])

print(max(dp[n]))

"""
** BFS 완전 탐색
"""
from collections import deque

queue = deque([(100, 0, 0)])  # 체력, 기쁨, 레벨
for i in range(n):
    while queue and queue[0][2] == i:
        cur_l, cur_j, cur = queue.popleft()
        queue.append((cur_l, cur_j, cur + 1))
        if cur_l - l[i] > 0:
            queue.append((cur_l - l[i], cur_j + j[i], cur + 1))

max_joy = 0
for _, x, _ in queue:
    if max_joy < x:
        max_joy = x

print(max_joy)
