#풀참
def solution(n, coins, m):
    dp = [10001] * (m + 1)
    dp[0] = 0
    for i in range(n):
        for k in range(coins[i], m + 1): 
            dp[k] = min(dp[k], dp[k - coins[i]] + 1)
        print(dp)
    if dp[m] == 10001:
        return -1
    else:
        return dp[m]
    
n, m = map(int, input().split())
coins = []
for _ in range(n):
    coins.append(int(input()))
print(solution(n, coins, m))