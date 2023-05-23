"""
2212. 센서
** Greedy
"""
import sys
input = sys.stdin.readline


n = int(input())
k = int(input())
pos = list(map(int, input().split()))

pos.sort()

# 구간 차이 구해서
diffs = []
for i in range(1, n):
    diffs.append(pos[i] - pos[i - 1])

diffs.sort(reverse=True)
# 상위 (k - 1)개 버리고 더하기
print(sum(diffs[k - 1:]))
