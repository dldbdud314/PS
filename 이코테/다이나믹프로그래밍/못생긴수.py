#dp로 안 푼 dp 문제랄ㄲㅏ..
import math
def erathosthenes(): #에라토스테네체의 체
    n = 1000
    arr = [True for _ in range(n + 1)]
    for i in range(2, int(math.sqrt(n)) + 1):
        if arr[i] == True:
            j = 2
            while i * j <= n:
                arr[i * j] = False
                j += 1
    primes = []
    for i in range(2, n + 1):
        if arr[i]:
            primes.append(i)
    return primes

#주어진 숫자 이하의 prime number만
#2, 3, 5 이외의 소수로 나눠지면 무조건 False
def is_ugly(num, primes):
    for prime in primes:
        if prime > num:
            break
        else:
            if num % prime == 0:
                return False
    return True

def solution(n):
    num = 0
    cnt = 0
    primes = erathosthenes()[3:] #1000 이하의 소수 집합 (2, 3, 5 제외)
    while cnt < n:
        num += 1
        if is_ugly(num, primes):
            cnt += 1
    return num

n = int(input())
print(solution(n))