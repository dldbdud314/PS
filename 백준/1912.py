"""
1912. 연속합

<< DP >>
- dp[i]: i번쨰 인덱스까지의 수 중 최대 연속합
- dp[i] = max(dp[i-1] + cur, cur)  -> (기존 DP 값 + 현재 수) VS. 현재 수부터 시작하는 경우
"""
import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

dp = [0] * n
dp[0] = nums[0]
for i in range(1, n):
    dp[i] = max(dp[i-1] + nums[i], nums[i])

print(max(dp))
