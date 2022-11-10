# 문자열 폭발

total = input()
bomb = input()

last_letter = bomb[-1]
stringStack = []
for x in total:
    stringStack.append(x)
    if x == last_letter and len(stringStack) >= len(bomb):
        if ''.join(stringStack[-len(bomb):]) == bomb:
            del stringStack[-len(bomb):]

print(''.join(stringStack)) if stringStack else print('FRULA')

# 특이사항: 똑같은 로직을 stringStack을 문자열로 구현하면, 문자열은 immutable로 하나하나 복사하는 과정을 거치기 때문에 시간초과가 뜨더라 !
