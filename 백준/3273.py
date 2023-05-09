"""
3273. 두 수의 합
- 해시
"""
import sys

input = sys.stdin.readline

n = int(input())
numbers = list(map(int, input().split()))
x = int(input())

cnt = 0
dic = [False] * 1000001
for number in numbers:
    if x - number < 1000001 and dic[x - number]:
        cnt += 1
    dic[number] = True

print(cnt)