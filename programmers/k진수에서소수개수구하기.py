import math

def get_knum(n, k):
    knum = ''
    while True:
        if n // k > 0:
            knum = str(n % k) + knum
            n //= k
        else:
            knum = str(n) + knum
            break
    return knum

def is_prime(n):
    for i in range(2, int(math.sqrt(n)) + 1): #제곱근까지만 체크해도 시간 많이 단축할 수 있음
        if n % i == 0:
            return 0
    return 1

def solution(n, k):
    #k진수 변환
    count = 0
    knum = get_knum(n, k) if 3 <= k < 10 else str(n)
    cnum = ''
    for x in knum + '0':
        if x != '0':
            cnum += x
        else:
            if len(cnum) > 0:
                if cnum == '1':
                    cnum = ''
                    continue
                count += is_prime(int(cnum)) #소수면 1 반환, 아니면 0
                cnum = ''
    return count
