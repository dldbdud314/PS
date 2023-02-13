'''
1758. 알바생 강호
- 그리디
'''
import sys
input = sys.stdin.readline


n = int(input())
p = [int(input()) for _ in range(n)]

p.sort(reverse=True)

total = 0
for idx, x in enumerate(p):
    m = x - idx
    if m < 0:
        continue
    total += m

print(total)
