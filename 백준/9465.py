"""
9465. 스티커
** DP -> 이전에 위쪽 스티커를 붙인 경우, 아래쪽에 스티커를 붙인 경우, 안 붙인 경우
- dp[0][i] = max(dp[1][i-1] + stickers[0][i], max(dp[0][i-2], dp[1][i-2]) + stickers[0][i]) (위)
- dp[1][i] = max(dp[0][i-1] + stickers[1][i], max(dp[0][i-2], dp[1][i-2]) + stickers[1][i]) (아래)
"""
import sys
input = sys.stdin.readline


def solution():
    n = int(input())
    stickers = [list(map(int, input().split())) for _ in range(2)]

    dp = [[0] * n for _ in range(2)]
    dp[0][0], dp[1][0] = stickers[0][0], stickers[1][0]
    for i in range(1, n):
        # 위
        dp[0][i] = max(dp[1][i - 1] + stickers[0][i], max(dp[0][i - 2], dp[1][i - 2]) + stickers[0][i] if i - 2 >= 0 else 0)
        # 아래
        dp[1][i] = max(dp[0][i - 1] + stickers[1][i], max(dp[0][i - 2], dp[1][i - 2]) + stickers[1][i] if i - 2 >= 0 else 0)

    return max(dp[0][-1], dp[1][-1])


T = int(input())
for _ in range(T):
    print(solution())
