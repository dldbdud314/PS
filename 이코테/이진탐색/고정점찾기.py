import sys

def solution(n, arr):
    start = 0
    end = n - 1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == mid:
            return mid
        if arr[mid] < mid:
            start = mid + 1
        else:
            end = mid - 1
    return -1

n = int(input())
arr = list(map(int, sys.stdin.readline().strip().split()))
print(solution(n, arr))