"""
3079. 입국심사
** 이분탐색, parametric search
"""
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
times = []
for _ in range(n):
    times.append(int(input()))

res = 0
l, r = 0, max(times) * m
while l <= r:
    mid = (l + r) // 2
    # mid 시간 동안 m명의 심사를 끝낼 수 있는지?
    checked, flag = 0, False
    for time in times:
        checked += (mid // time)
        if checked >= m:
            flag = True
            break

    if flag:
        res = mid
        r = mid - 1
    else:
        l = mid + 1

print(res)
