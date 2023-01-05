from collections import defaultdict


def is_identical(map1, map2):
    if len(map1) != len(map2):
        return False
    for k, v in map1.items():
        if k not in map2:
            return False
        if map2[k] != v:
            return False
    return True


def solution(want, number, discount):
    want_map = {w: n for w, n in zip(want, number)}

    cur_map = defaultdict(int)
    l, r = 0, sum(number)  # r은 끝점 + 1이라는 거 주의 !
    for i in range(l, r):
        cur_map[discount[i]] += 1

    res = 0
    while True:
        if is_identical(want_map, cur_map):
            res += 1

        to_remove = discount[l]
        cur_map[to_remove] -= 1
        if cur_map[to_remove] == 0: del cur_map[to_remove]
        l += 1

        if r >= len(discount):
            break
        to_add = discount[r]
        cur_map[to_add] += 1
        r += 1

    return res