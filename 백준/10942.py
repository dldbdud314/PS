"""
10942. 팰린드롬?
- 쿼리 개수 m이 최악의 경우 1,000,000 -> 그때그때 팰린드롬 여부를 판별하는 알고리즘 활용하기 까다롭다 (O(n) 불가 !)

** DP -> 풀참
- dp[s][e] : s부터 e까지의 부분 문자열이 팰린드롬인지 (True/False)
- dp[s][e] = dp[s+1][e-1] AND (처음 요소 == 끝 요소)
"""
import sys
input = sys.stdin.readline


n = int(input())
numbers = list(map(int, input().split()))

dp = [[False] * n for _ in range(n)]
for jump in range(n):
    for s in range(n):
        e = s + jump

        if e >= n:
            break

        if e == s:
            dp[s][e] = True
            continue

        if e - s == 1:
            dp[s][e] = True if numbers[s] == numbers[e] else False
            continue

        dp[s][e] = dp[s+1][e-1] and numbers[s] == numbers[e]


m = int(input())  # 쿼리 개수
for _ in range(m):
    s, e = map(int, input().split())
    # 팰린드롬 확인
    print(int(dp[s-1][e-1]))
