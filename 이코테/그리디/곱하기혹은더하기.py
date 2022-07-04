def solution(s):
    res = 0
    for i in range(len(s)-1):
        op1 = int(s[i]) if res == 0 else res
        op2 = int(s[i+1])
        if op1 == 0 or op2 == 0:
            res = (op1 + op2)
        else:
            res = (op1 * op2)
    return res
s = input()
print(solution(s))