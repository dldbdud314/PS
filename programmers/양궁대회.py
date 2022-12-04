from itertools import combinations_with_replacement


def get_score_diff(apeach_info, ryan_info):
    apeach_score, ryan_score = 0, 0
    for idx, (acnt, rcnt) in enumerate(zip(apeach_info, ryan_info)):
        if acnt == rcnt == 0:
            continue
        if acnt >= rcnt:
            apeach_score += (10 - idx)
        else:
            ryan_score += (10 - idx)

    return ryan_score - apeach_score if ryan_score > apeach_score else 0


def get_adequate_info(max_score_info, ryan_info):
    for x1, x2 in zip(reversed(max_score_info), reversed(ryan_info)):
        if x1 == x2 == 0:
            continue
        if x1 > x2:
            return max_score_info
        elif x1 < x2:
            return ryan_info


# 중복 조합 활용
def solution(n, info):
    max_score_diff = -float('inf')  # 가장 큰 점수 차
    max_score_info = []  # 가장 큰 점수 차일 때, ryan 의 점수 배열 기록 (max_score가 같은 경우, 비교하기 위해
    for combi in combinations_with_replacement(range(11), n):
        ryan_info = [0] * 11
        for idx in combi:
            ryan_info[idx] += 1  # ryan 이 맞힌 점수 배열

        cur_score_diff = get_score_diff(info, ryan_info)
        if cur_score_diff > 0:
            if max_score_diff < cur_score_diff:
                max_score_diff = cur_score_diff
                max_score_info = ryan_info
            elif max_score_diff == cur_score_diff:
                max_score_info = get_adequate_info(max_score_info, ryan_info)

    return [-1] if max_score_diff == -float('inf') else max_score_info


print(solution(5, [2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0]))
print(solution(1, [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))
print(solution(9, [0, 0, 1, 2, 0, 1, 1, 1, 1, 1, 1]))
print(solution(10, [0, 0, 0, 0, 0, 0, 0, 0, 3, 4, 3]))
