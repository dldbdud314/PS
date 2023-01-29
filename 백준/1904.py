# 01 타일
# 피보나치 수열과 동일
def calc(n):
    # edge case
    if n == 1:
        return 1

    dp = [0] * (n + 1)  # dp[i] = 만들 수 있는 가짓수
    dp[1] = 1
    dp[2] = 2

    for i in range(3, n + 1):
        dp[i] = (dp[i - 1] + dp[i - 2]) % 15746

    return dp[n]


n = int(input())
print(calc(n))
