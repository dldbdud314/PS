"""
2156. 포도주 시식

** DP
jump 한 경우, 연속으로 센 경우 나눠서 갱신
- dp[i][2] = dp[i-1][1] + num[i]
- dp[i][1] = max(dp[i-2]) + num[i]

+ 아예 안 마시는 경우를 빠뜨림..!
- dp[i][0] = max(dp[i-1])
"""
import sys
input = sys.stdin.readline


def solution():
    dp = [[0, 0, 0] for _ in range(n)]  # dp[i][cnt] : i번째까지 최대수, jump 횟수(=cnt) 포함
    dp[0][1] = num[0]
    if n == 1:
        return dp[0][1]
    dp[1][1], dp[1][2] = num[1], num[0] + num[1]
    if n == 2:
        return max(dp[1])

    max_amt = -float('inf')
    for i in range(2, n):
        dp[i][0] = max(dp[i - 1])  # 안 마신 경우
        dp[i][1] = max(dp[i - 2]) + num[i]  # 첫번째 잔
        dp[i][2] = dp[i - 1][1] + num[i]  # 두번째 잔

        cur = max(dp[i])
        if max_amt < cur:
            max_amt = cur

    return max_amt


n = int(input().rstrip())
num = []
for _ in range(n):
    num.append(int(input().rstrip()))

print(solution())
