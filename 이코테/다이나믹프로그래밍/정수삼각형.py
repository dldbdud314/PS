def solution(n, triangle):
    dp = [[0] * n for _ in range(n)]
    dp[0][0] = triangle[0][0]
    for i in range(1, n):
        for j in range(i + 1):
            dp[i][j] = max(dp[i-1][j-1] if j-1 >= 0 else 0, dp[i-1][j]) + triangle[i][j]
    return max(dp[n-1])

n = int(input())
triangle = []
for _ in range(n):
    triangle.append(list(map(int, input().split())))
print(solution(n, triangle))