import sys

def solution(n, arr, ranges):
    sums = [0] * (n + 1)
    for i in range(1, n + 1):
        sums[i] = sums[i-1] + arr[i-1]
    for a, b in ranges:
        print(sums[b] - sums[a-1])

n = int(input())
arr = list(map(int, sys.stdin.readline().split()))
m = int(input())
ranges = []
for _ in range(m):
    a, b = map(int, input().split())
    ranges.append([a, b])
solution(n, arr, ranges)