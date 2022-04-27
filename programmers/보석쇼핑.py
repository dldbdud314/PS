"""
1. set(gems) - 종류
2. l, r 늘려가며 dictionary 갱신!
"""
#투포인터 알고리즘
def solution(gems):
    length = len(set(gems))
    l, r, min_len = 0, 0, float('inf')
    min_range = [0, 0]
    cur_map = dict()
    cur_map[gems[0]] = 1
    while r < len(gems) and l <= r:
        if len(cur_map) == length:
            if r + 1 - l < min_len: 
                min_len = r + 1 - l
                min_range = [l + 1, r + 1]
        if len(cur_map) < length and r + 1 < len(gems):
            r += 1
            if gems[r] in cur_map: cur_map[gems[r]] += 1
            else: cur_map[gems[r]] = 1
        else:
            if cur_map[gems[l]] == 1: del cur_map[gems[l]]
            else: cur_map[gems[l]] -= 1
            l += 1         
    return min_range
