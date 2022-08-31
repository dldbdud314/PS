def solution(n, coins, m):
    dp = [10001] * (m + 1)
    dp[0] = 0
    for i in range(n):
        for j in range(coins[i], m + 1):
            dp[j] = min(dp[j], dp[j - coins[i]] + 1)
    return -1 if dp[m] == 10001 else dp[m]

n, m = map(int, input().split())
coins = []
for _ in range(n):
    coins.append(int(input()))
print(solution(n, coins, m))