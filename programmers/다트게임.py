def after_bonus(num, bonus):
    if bonus == 'S':
        return num
    elif bonus == 'D':
        return num * num
    elif bonus == 'T':
        return num * num * num

def solution(dartResult):
    dartResult = dartResult.replace('10', '!') # 파싱하기 쉽게 자릿수 맞추기
    # 선파싱
    parsed = []
    tmp = ''
    for x in dartResult:
        if x == '!' or x.isdigit() and len(tmp) > 0:
            parsed.append(tmp)
            tmp = x
        else:
            tmp += x
    parsed.append(tmp)
    
    # 연산
    res = []
    for x in parsed: 
        if len(x) == 2:
            num, bonus = int(x[0]) if x[0] != '!' else 10, x[1]
            num = after_bonus(num, bonus)
            res.append(num)
        elif len(x) == 3:
            num, bonus, op = int(x[0]) if x[0] != '!' else 10, x[1], x[2]
            num = after_bonus(num, bonus)
            if op == '*':
                if res: 
                    res[-1] = res[-1] * 2
                num = num * 2
            elif op == '#': 
                num = num * (-1)
            res.append(num)
    
    return sum(res)