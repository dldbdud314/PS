"""
** Tree 성질 응용, recursive
"""


def is_all_null(bnum):  # 양쪽 자식 트리 검사
    half = len(bnum) // 2
    return bnum[:half].count('0') == bnum[half + 1:].count('0') == half


def is_valid_bt(bnum):
    if len(bnum) == 1:  # 길이가 1이면 상관없이 통과
        return True

    mid = len(bnum) // 2
    # 부모 null + 양쪽 자식 트리 모두 null 이면 PASS, 하나라도 노드가 존재하면 FALSE
    if bnum[mid] == '0' and not is_all_null(bnum):
        return False

    return is_valid_bt(bnum[:mid]) and is_valid_bt(bnum[mid + 1:])


def find_upper(n):  # 포화 이진 트리 맞추기 위해
    h = 0
    while 2 ** h - 1 < n: h += 1
    return 2 ** h - 1


def solution(numbers):
    res = []
    for number in numbers:
        bnum = format(number, 'b')
        bnum = '0' * (find_upper(len(bnum)) - len(bnum)) + bnum  # 포화 이진 트리 노드 개수 맞추기

        res.append(int(is_valid_bt(bnum)))

    return res

