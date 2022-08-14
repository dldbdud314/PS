from collections import Counter
def solution(X, Y):
    num_str = ''
    xcnt, ycnt = Counter(X), Counter(Y)
    for xk in xcnt.keys():
        if xk in ycnt:
            num_str += (xk * min(xcnt[xk], ycnt[xk]))
    if num_str:
        return int(''.join(sorted(list(num_str), reverse = True)))
    else:
        return -1
    
print(solution('5525', '1255'))
# 73.7 / 100