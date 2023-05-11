"""
** 구현 (수학) -> 약수
"""
import math


# 자기자신을 제외한 가장 큰 약수 -> 그리디
def get_largest_divisor(n):
    if n == 1:
        return 0
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0 and n // i <= 10 ** 7:
            return n // i
    return 1


def solution(begin, end):
    res = []
    for n in range(begin, end + 1):
        res.append(get_largest_divisor(n))

    return res

# 13번, 효율성 FAIL -> https://school.programmers.co.kr/questions/43745
