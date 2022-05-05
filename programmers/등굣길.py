def solution(m, n, puddles):
    dp = [[0] * (m+1) for _ in range(n+1)]
    dp[1][1] = 1 #dp[x][y] = 여기까지 오는 방법의 수
    for i in range(1, n+1):
        for j in range(1, m+1):
            if [j, i] in puddles or [i, j] == [1, 1]:
                continue
            else:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
    return dp[-1][-1] % 1000000007
