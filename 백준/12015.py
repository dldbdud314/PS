# 가장 긴 증가하는 부분수열 2 -> 이분탐색 !
import sys
from bisect import bisect_left

n = int(input())
arr = list(map(int, sys.stdin.readline().split()))

lst = [0]

for a in arr:
    if lst[-1] < a:
        lst.append(a)
    else:
        lst[bisect_left(lst, a)] = a

print(len(lst) - 1)