"""
20922. 겹치는 건 싫어

** 투포인터
- 뺄 때 매번 validation 검사 -> 시간초과
- 수정 : r을 늘려서 추가할 때 validation 확인, 만족할 때까지 l 늘리기 -> PASS !
"""
from collections import defaultdict
import sys

input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(map(int, input().split()))


l, r = 0, 0
cur = defaultdict(int)
cur[arr[0]] += 1
max_len = 1
while l <= r < n:
    r += 1
    max_len = max(r - l, max_len)
    if r == n:
        break
    cur[arr[r]] += 1
    while cur[arr[r]] > k:
        cur[arr[l]] -= 1
        l += 1


print(max_len)
