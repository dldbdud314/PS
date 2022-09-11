import math
def erathosthenes():
    n = 1000 #1000 이하의 소수 집합 구하기
    arr = [True for _ in range(n + 1)] #arr[i] == True인 경우 소수라고 간주
    for i in range(2, int(math.sqrt(n)) + 1):
        if arr[i] == True:
            j = 2
            while i * j <= n:
                arr[i * j] = False #소수의 n-배수는 소수가 아니다
                j += 1
    primes = []
    for i in range(2, n + 1):
        if arr[i]: primes.append(i)
    return primes