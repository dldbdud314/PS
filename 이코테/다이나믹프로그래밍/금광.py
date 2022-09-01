def to_matrix(n, m, arr):
    matrix = []
    k = 0
    for _ in range(n):
        matrix.append(arr[k:k+m])
        k += m
    return matrix

T = int(input())
ans = []
for _ in range(T):
    n, m = map(int, input().split())
    matrix = []
    idx = 0
    matrix = to_matrix(n, m, list(map(int, input().split())))
    dp = [[0] * m for _ in range(n)]
    for i in range(n):
        dp[i][0] = matrix[i][0]
    for j in range(1, m):
        for i in range(n):
            upper_left = dp[i-1][j-1] if i - 1 >= 0 else 0
            left = dp[i][j-1]
            lower_left = dp[i+1][j-1] if i + 1 < n else 0
            dp[i][j] = max(upper_left, left, lower_left) + matrix[i][j]
    ans.append(max([dp[k][-1] for k in range(n)]))
for a in ans:
    print(a)