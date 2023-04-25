'''
** Greedy
'''
from collections import deque


def calc(cur_p, cur_m):
    if cur_p == 'diamond':
        return cur_m[0] * 1 + cur_m[1] * 1 + cur_m[2] * 1
    if cur_p == 'iron':
        return cur_m[0] * 5 + cur_m[1] * 1 + cur_m[2] * 1
    if cur_p == 'stone':
        return cur_m[0] * 25 + cur_m[1] * 5 + cur_m[2] * 1


def counter(arr):
    count = [0] * 3  # [d, i, s] 순으로 개수
    for x in arr:
        if x == 'diamond':
            count[0] += 1
        elif x == 'iron':
            count[1] += 1
        else:
            count[2] += 1
    return count


def solution(picks, minerals):
    # minerals 5개 묶음으로 전처리 (비용 큰 순 정렬)
    mineral_data = []
    cnt, i = 0, 0  # 곡괭이 개수만큼 짜르기 !! (minerals 전체 짜르기 -> TC8 반례)
    while cnt < sum(picks) and i < len(minerals):
        mineral_data.append(counter(minerals[i:i+5]))
        i += 5
        cnt += 1
    mineral_data.sort(reverse=True)
    mq = deque(mineral_data)

    # picks -> 개수만큼 배열로
    pq = deque(picks[0] * ['diamond'] + picks[1] * ['iron'] + picks[2] * ['stone'])

    # Greedy 수행
    fatigue = 0
    while pq and mq:
        px = pq.popleft()
        mx = mq.popleft()

        fatigue += calc(px, mx)

    return fatigue


print(solution([0, 1, 1], ["diamond", "diamond", "diamond", "diamond", "diamond", "iron", "iron", "iron", "iron", "iron", "diamond"]))
