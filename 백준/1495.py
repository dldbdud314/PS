"""
1495. 기타리스트
** BFS (+cutting-edge)
"""
from collections import deque
import sys
input = sys.stdin.readline


n, s, m = map(int, input().split())
v = list(map(int, input().split()))

queue = deque([(s, 0)])
prev = 0  # 기존 레벨
for i in range(n):
    d = v[i]
    visited = set()  # 동레벨 내에서 중복 연산 제거 (->없으면 메모리 초과 발생)
    while queue and queue[0][1] == prev:
        cur, l = queue.popleft()
        if cur - d >= 0 and cur - d not in visited:
            queue.append((cur - d, l + 1))
            visited.add(cur - d)
        if cur + d <= m and cur + d not in visited:
            queue.append((cur + d, l + 1))
            visited.add(cur + d)
    prev += 1

print(max(list(map(lambda x: x[0], queue)))) if queue else print(-1)

"""
** DP -> 풀이 참고
- dp[i][j] : i번째 레벨에서 j라는 수를 만들 수 있는가? 
"""
dp = [[False] * (m + 1) for _ in range(n + 1)]
dp[0][s] = True
for i in range(1, n + 1):
    for j in range(m + 1):
        if dp[i - 1][j]:
            if j - v[i - 1] >= 0:
                dp[i][j - v[i - 1]] = True
            if j + v[i - 1] <= m:
                dp[i][j + v[i - 1]] = True

res = -1
for k in range(m + 1):
    if dp[n][k]:
        res = k
print(res)
