"""
** 브루트포스
"""


def solution(s):
    mapper = {'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7',
              'eight': '8', 'nine': '9'}

    res = ''
    tmp = ''
    for c in s:
        if c.isdigit():
            res += c
            continue

        tmp += c
        if len(tmp) >= 3 and tmp in mapper:
            res += mapper[tmp]
            tmp = ''

    return int(res)
