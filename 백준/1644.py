#소수의연속합
import math

def prime_numbers(k): #에라토스테네스의 체
    n = k
    arr = [True for _ in range(n + 1)]
    for i in range(2, int(math.sqrt(n)) + 1):
        if arr[i]:
            j = 2
            while i * j <= n:
                arr[i * j] = False
                j += 1
    primes = []
    for i in range(2, n + 1):
        if arr[i]:
            primes.append(i)
    return primes

def solution(n):
    cnt = 0
    if n == 1: return cnt #edge case
    primes = prime_numbers(n)
    l, r = 0, 0
    total = primes[0]
    while r < len(primes) and l <= r:
        if total == n:
            cnt += 1
        if total < n and r + 1 < len(primes):
            r += 1
            total += primes[r]
        else:
            total -= primes[l]
            l += 1
    return cnt

n = int(input())
print(solution(n))