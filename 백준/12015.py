# 가장 긴 증가하는 부분수열 2 -> 이분탐색 !
import sys
from bisect import bisect_left

n = int(input())
arr = list(map(int, sys.stdin.readline().split()))

dp = [0]

for a in arr:
    if dp[-1] < a:
        dp.append(a)
    else:
        dp[bisect_left(dp, a)] = a

print(len(dp) - 1)