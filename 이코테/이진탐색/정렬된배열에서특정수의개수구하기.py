import sys
from bisect import bisect_right, bisect_left

def count_by_range(a, l, r):
    right_idx = bisect_right(a, r)
    left_idx = bisect_left(a, l)
    return right_idx - left_idx

def solution(x, arr):
    if x < arr[0] or x > arr[-1]: return -1
    return count_by_range(arr, x, x)

n, x = map(int, input().split())
arr = list(map(int, sys.stdin.readline().strip().split()))
print(solution(x, arr))