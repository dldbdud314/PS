"""
그리디 (큐 활용)
"""
from collections import deque


def solution(n, m, section):
    cnt = 1
    queue = deque(section)
    cur = queue.popleft()
    s, e = cur, cur + m
    while queue:
        cur = queue.popleft()

        if s <= cur < e:
            continue

        s, e = cur, cur + m  # 갱신
        cnt += 1

    return cnt
