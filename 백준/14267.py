"""
14267. 회사 문화 1
** DFS + DP

1) 매 칭찬마다 dfs -> 시간 초과
2) 풀참 => 미리 DP 배열에 칭찬 저장, dfs 한번으로 dp 칭찬 누적
"""
import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline


n, m = map(int, input().split())

tree = [list() for _ in range(n)]  # 상사-부하 관계
info = list(map(int, input().split()))
for i in range(1, n):
    tree[info[i] - 1].append(i)

dp = [0] * n  # 누적 칭찬


def dfs(cur):
    for nxt in tree[cur]:
        dp[nxt] += dp[cur]  # 직속 부하에게 칭찬 누적
        dfs(nxt)


for _ in range(m):
    p, w = map(int, input().split())
    dp[p - 1] += w

dfs(0)  # 시간 초과 수정 -> dfs 한번

print(*dp)
