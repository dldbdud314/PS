"""
** 구현 (수학)
- arrayA, arrayB 최대공약수 구하기 -> gcd1, gcd2
- gcd1, gcd2 로 다른 배열 중 하나라도 나누어지면 FAIL ! 나누어 떨어지면 gcd 그대로 RETURN
"""
import math


# 다른 배열의 수를 나눌 수 있으면 FAIL
def divide(d, arr):
    for x in arr:
        if x % d == 0:
            return 0
    return d


def solution(arrayA, arrayB):
    gcd1, gcd2 = arrayA[0], arrayB[0]  # 최대공약수
    for i in range(1, len(arrayA)):
        gcd1 = math.gcd(arrayA[i], gcd1)
        gcd2 = math.gcd(arrayB[i], gcd2)

    return max(divide(gcd1, arrayB), divide(gcd2, arrayA))
