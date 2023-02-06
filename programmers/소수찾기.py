from itertools import permutations
from math import sqrt


def is_prime(n):  # 효율적인 소수 판별 알고리즘
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True


def solution(numbers):
    nlst = list(numbers)
    cnt = 0
    v = set()  # 중복 제거 1
    for pick in range(1, len(numbers) + 1):
        for combi in set(permutations(nlst, pick)):  # 중복 제거 2
            cur_num = int(''.join(combi))
            if cur_num < 2 or cur_num in v:
                continue
            v.add(cur_num)
            if is_prime(cur_num):
                cnt += 1

    return cnt


# print(solution("17"))
print(solution("011"))
