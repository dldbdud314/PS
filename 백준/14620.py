from itertools import combinations
import sys

input = sys.stdin.readline

min_sum = float('inf')

n = int(input())
MAP = [list(map(int, input().split())) for _ in range(n)]


def add_pos(p):
    total = 0
    for y, x in p:
        total += MAP[y][x]
    return total


positions = [(y, x) for x in range(1, n - 1) for y in range(1, n - 1)]
for k in combinations(positions, 3):
    p_total = set()
    for cy, cx in k:
        p_total.add((cy, cx))
        for dy, dx in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            p_total.add((dy + cy, dx + cx))
    if len(p_total) < 5 * 3:
        continue
    cur_sum = add_pos(p_total)
    if cur_sum < min_sum:
        min_sum = cur_sum

print(min_sum)