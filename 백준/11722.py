#가장 긴 감소하는 부분수열
def solution(n, arr):
    dp = [1] * n
    for i in range(1, len(arr)):
        for j in range(i):
            if arr[j] > arr[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)
    
n = int(input())
arr = list(map(int, input().split()))
print(solution(n, arr))