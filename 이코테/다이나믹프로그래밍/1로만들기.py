# 해답 풀이
def solution(x):
    d = [0] * (x + 1)
    for i in range(2, x + 1):
        d[i] = d[i - 1] + 1
        if i % 2 == 0:
            d[i] = min(d[i], d[i // 2] + 1)
        if i % 3 == 0:
            d[i] = min(d[i], d[i // 3] + 1)
        if i % 5 == 0:
            d[i] = min(d[i], d[i // 5] + 1)
    return d[x]


# dp[x] = x를 1로 만드는 데 최소 연산 횟수
# my 풀이 (접근은 똑같음)
def _solution(x):
    dp = [0] * (x + 1)
    for i in range(2, x + 1):
        candidates = []
        if i % 5 == 0:
            candidates.append(dp[i // 5])
        if i % 3 == 0:
            candidates.append(dp[i // 3])
        if i % 2 == 0:
            candidates.append(dp[i // 2])
        candidates.append(dp[i - 1])

        dp[i] = min(candidates) + 1

    return dp[x]

    
x = int(input())
print(solution(x))