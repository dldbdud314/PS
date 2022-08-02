#부품찾기
import sys

#1. 이진탐색
def solution1(n, a, b):
    a.sort()
    for x in b:
        start, end = 0, n - 1
        while start <= end:
            mid = (start + end) // 2
            if x == a[mid]:
                print("yes", end = ' ')
                break
            if x < a[mid]:
                end = mid - 1
            else:
                start = mid + 1
        else: #못 찾으면
            print("no", end = ' ')

#2. 계수정렬 변형       
def solution2(a, b):
    flags = [False] * 100001
    for x in a:
        flags[x] = True
    for y in b:
        if flags[y]: print("yes", end = ' ')
        else: print("no", end = ' ')

n = int(input())
a = list(map(int, sys.stdin.readline().strip().split()))
m = int(input())
b = list(map(int, sys.stdin.readline().strip().split()))

print("solution1 (binary search) : ")
solution1(n, a, b)
print("\nsolution2 (count sort) : ")
solution2(a, b)