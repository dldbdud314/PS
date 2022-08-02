#떡볶이 떡 만들기
#parametric search 
import sys

def cut(arr, mid):
    res = 0
    for a in arr:
        if a > mid:
            res += (a - mid)
    return res

def solution(n, m, arr):
    arr.sort()
    start = 0
    end = arr[n - 1]
    res = 0
    while start <= end:
        mid = (start + end) // 2
        total_len = cut(arr, mid)
        if total_len >= m:
            res = mid
            start = mid + 1
        else:
            end = mid - 1
    return res

n, m = map(int, input().split())
arr = list(map(int, sys.stdin.readline().strip().split()))
print(solution(n, m, arr))