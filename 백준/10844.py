"""
10844. 쉬운 계단 수 - 풀참 !

** DP
앞에 오는 수에 따라 다른 경우의 수를 취해야 ! --> 2차원 DP 배열 활용 !
- dp[자리수][0] = dp[자리수-1][1]
- dp[자리수][k] = dp[자리수-1][k-1] + dp[자리수-1][k+1] (1 <= k <= 8)
- dp[자리수][9] = dp[자리수-1][8]
"""
n = int(input())
dp = [[0] * 10 for _ in range(n + 1)]  # dp[자릿수][마지막 수] = 경우의 수
for i in range(1, 10):
    dp[1][i] = 1

for m in range(2, n + 1):
    for k in range(10):
        if k == 0:
            dp[m][k] = dp[m - 1][1]
        elif k == 9:
            dp[m][k] = dp[m - 1][8]
        else:
            dp[m][k] = dp[m - 1][k - 1] + dp[m - 1][k + 1]

print(sum(dp[n]) % 1_000_000_000)
