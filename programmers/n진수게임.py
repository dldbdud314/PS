def getNbase(n, q):
    if n == 0: return '0'
    rev_base = ''
    while n > 0:
        n, mod = divmod(n, q)
        rev_base += hex(mod)[2:].upper()
    return rev_base[::-1]

def solution(n, t, m, p):
    num = 0
    cnt = 0
    res = ''
    while num <= t * m:
        nBaseNum = getNbase(num, n)
        for x in nBaseNum:
            if (cnt // m) == t: break
            if cnt % m == (p - 1):
                res += x
            cnt += 1
        num += 1
    return res

print(solution(16, 16, 2, 2))