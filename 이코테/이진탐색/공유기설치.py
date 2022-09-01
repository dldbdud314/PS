#백준 2110
#parametric search
import sys

def count_house(m, houses):
    last = houses[0]
    count = 1
    for i in range(1, len(houses)):
        if (houses[i] - last) >= m:
            last = houses[i]
            count += 1
    return count

def solution(n, c, houses):
    houses.sort()
    s = 0
    e = houses[-1] - houses[0]
    d = 0
    while s <= e:
        m = (s + e) // 2
        count = count_house(m, houses)
        if count >= c:
            if m > d: d = m
            s = m + 1
        else:
            e = m - 1
    return d

n, c = map(int, input().split())
houses = []
for _ in range(n):
    houses.append(int(sys.stdin.readline()))
print(solution(n, c, houses))