# 지름길
def solution(n, m, paths):
    dp = [x for x in range(m + 1)]

    for pos in range(1, m + 1):  # pos : 현위치
        dp[pos] = dp[pos - 1] + 1
        for start, end, length in paths:
            if end == pos:
                dp[end] = min(dp[end], dp[start] + length)

    return dp[m]


n, m = map(int, input().split())
paths = []
for _ in range(n):
    paths.append(list(map(int, input().split())))
print(solution(n, m, paths))
