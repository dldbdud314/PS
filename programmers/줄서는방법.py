"""
** 구현(수학) -> 풀이 참고
- 현재 자릿수 n 기준 나올 수 있는 경우의 수 -> factorial(n - 1)
- k // factorial(n - 1)번째 수 -> n번째 자리의 숫자
- k %= factorial(n - 1)
"""
from math import factorial


def solution(n, k):
    res = []
    choices = [i for i in range(1, n + 1)]  # 사용할 수 있는 숫자 목록
    while n != 0:
        num = factorial(n - 1)
        idx = k // num if k % num > 0 else k // num - 1
        res.append(choices.pop(idx))
        n -= 1
        k %= num

    return res

# 초기 규칙성 틀림,, 규칙성 찾는 게 중요 !!
