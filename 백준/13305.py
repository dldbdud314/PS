'''
13305. 주유소
- 그리디 (min heap 활용)
'''
from heapq import heappop, heappush
import sys

input = sys.stdin.readline

q = []  # (비용, idx) min heap

n = int(input())
roads = list(map(int, input().split()))
towns = list(map(int, input().split()))
for i, cost in enumerate(towns):
    if i == n - 1:  # 마지막 도시 제외
        break
    heappush(q, (cost, i))  # 최소 비용 순

total = 0
last_idx = n - 1  # 도로의 마지막 인덱스
while q:
    cost, idx = heappop(q)

    if idx < last_idx:
        total += sum(roads[idx: last_idx]) * cost
        last_idx = idx

print(total)
