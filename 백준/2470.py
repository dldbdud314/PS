"""
2470. 두 용액
** 정렬 활용
"""
import sys

input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))

data = sorted(data, key=lambda x: abs(x))

diff = int(1e20)
res = []
for i in range(1, len(data)):
    cur = data[i - 1] + data[i]
    if abs(cur) < diff:
        diff = abs(cur)
        res = [data[i - 1], data[i]]

res.sort()
print(*res, sep=' ')
