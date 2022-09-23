def solution(n, s):
    if n > s:
        return [-1]
    ans = []
    while True:
        if n == 0:
            break
        p = s // n
        ans.append(p)
        s -= p
        n -= 1
    return ans
