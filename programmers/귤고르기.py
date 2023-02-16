'''
그리디 : 많이 나온 순으로 SORTING 후, 앞에서부터 k개 뽑아 중복 제거
'''
from collections import Counter


def solution(k, tangerine):
    tangerines_sorted = []
    for val, cnt in Counter(tangerine).most_common():
        tangerines_sorted.extend([val] * cnt)

    return len(set(tangerines_sorted[:k]))
