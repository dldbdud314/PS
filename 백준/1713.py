"""
1713. 후보 추천하기
** 완전탐색
"""
from collections import defaultdict


def solution():
    records = defaultdict(int)  # 추천 횟수 기록
    photos = []  # 후보들
    for x in arr:
        if x in photos:  # 이미 있으면 추천 수만 늘리고 PASS
            records[x] += 1
            continue

        # 꽉 차서 교체 필요
        if len(photos) == n:
            min_cnt = float('inf')
            out = -1
            for photo in photos:  # 제일 적은 추천 수 찾아서
                if records[photo] < min_cnt:
                    min_cnt = records[photo]
                    out = photo
            photos.remove(out)  # 제거
            records[out] = 0  # 초기화

        photos.append(x)
        records[x] += 1

    return sorted(photos)


n = int(input())
cnt = int(input())
arr = list(map(int, input().split()))

print(*solution())
