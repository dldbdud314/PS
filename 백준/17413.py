#단어 뒤집기 2
s = input()

tmp, ans = '', ''
flag = False
for x in s:
    if x == '<':
        flag = True
        if len(tmp) > 0:
            ans += tmp[::-1]
        tmp = x
    elif x == '>':
        flag = False
        tmp += x
        ans += tmp
        tmp = ''
    else:
        if x == ' ':
            if flag: #괄호 내인 경우
                tmp += x
            else:
                if len(tmp) > 0:
                    ans += tmp[::-1] + ' '
                    tmp = ''
        else:
            tmp += x
if len(tmp) > 0:
    ans += tmp[::-1]
        
print(ans)