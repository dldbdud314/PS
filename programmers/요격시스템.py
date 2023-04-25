'''
** Greedy (스케쥴링 문제) : 아이디어 떠올리지 X -> 풀참
- 끝점 기준 정렬, 마지막 끝점 <= 시작점 기준 그리디
'''


def solution(targets):
    targets.sort(key=lambda x: (x[1], x[0]))

    cnt = 0
    pe = 0  # 마지막 끝점
    for s, e in targets:
        if pe <= s:
            cnt += 1
            pe = e

    return cnt
