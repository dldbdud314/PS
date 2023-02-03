"""
2193. 이친수
1st ) Fail

<< DP >>
- dp[i]: i자리 이친수 목록
- dp[i-1] 목록들을 돌아가며 0/1 추가. 단, 1은 연속되지 않는 경우 추가하기

-> 메모리 초과로 하다 못해 캐시 활용 했는데 최악의 경우 2 ^ 90이라 메모리 초과 나는 듯
"""

n = int(input())

cache = {'1'}

for _ in range(2, n + 1):
    new_cache = set()
    for x in cache:
        if x[-1] != '1':
            new_cache.add(x + '1')
        new_cache.add(x + '0')
    cache = new_cache

print(len(cache))

"""
사실 스포 당함 -> 피보나치 수열
"""


def fibonacci(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2

    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[n - 2]

    return dp[n]


n = int(input())
print(fibonacci(n))
