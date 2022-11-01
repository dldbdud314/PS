# 상자넣기
def solution(n, boxes):
    dp = [1 for _ in range(n)]
    for i in range(n):
        for j in range(i):
            if boxes[i] > boxes[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)


n = int(input())
boxes = list(map(int, input().split()))
print(solution(n, boxes))