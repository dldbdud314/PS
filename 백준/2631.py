# 줄세우기
def solution(n, line):
    dp = [1 for _ in range(n)]
    for i in range(n):
        for j in range(i):
            if line[i] > line[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return n - max(dp)


n = int(input())
line = []
for _ in range(n):
    line.append(int(input()))
print(solution(n, line))