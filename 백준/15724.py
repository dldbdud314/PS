"""
15724. 주지수
** Prefix Sum
"""
import sys
input = sys.stdin.readline


n, m = map(int, input().split())
p_sum = [[0] * (m + 1) for _ in range(n + 1)]

ppl = [list(map(int, input().split())) for _ in range(n)]

# prefix sum 만들기
for i in range(1, n + 1):
    for j in range(1, m + 1):
        p_sum[i][j] = p_sum[i - 1][j] + p_sum[i][j - 1] - p_sum[i - 1][j - 1] + ppl[i - 1][j - 1]

# 누적합 계산
k = int(input())
for _ in range(k):
    sx, sy, ex, ey = map(int, input().split())
    print(p_sum[ex][ey] - p_sum[sx - 1][ey] - p_sum[ex][sy - 1] + p_sum[sx - 1][sy - 1])
