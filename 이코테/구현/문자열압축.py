def solution(s):
    shortest = len(s)
    for i in range(1, len(s)//2 + 1):
        res = ''
        cnt = 1
        for j in range(i, len(s), i):
            if s[j-i : j] == s[j : j+i]:
                cnt += 1
            else:
                if cnt > 1:
                    res += (str(cnt) + s[j-i : j])
                else:
                    res += s[j-i : j]
                cnt = 1
        if cnt > 1: res += (str(cnt) + s[j-i : j])
        else: res += s[j : j+i]
        shortest = min(shortest, len(res))
    return shortest
s = input()
print(solution(s))

