#동전0
def solution(arr, k):
    arr.sort(reverse=True)
    res = 0
    for x in arr:
        if k == 0: break
        if k // x > 0:
            res += (k // x)
            k %= x
    return res

n, k = map(int, input().split())
arr = [int(input()) for _ in range(n)]
print(solution(arr, k))