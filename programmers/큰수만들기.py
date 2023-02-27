'''
** 그리디 기반 스택 : 아이디어 떠올리기 힘듦,,
stack : 되도록이면 큰 수가 앞에 오도록
'''


def solution(number, k):
    number = list(map(int, list(number)))

    stack = []
    for i in range(len(number)):
        while stack and stack[-1] < number[i] and k > 0:
            stack.pop()
            k -= 1
        if k == 0:
            stack += number[i:]
            break
        stack.append(number[i])

    if k > 0:
        stack = stack[:-k]

    return ''.join(list(map(str, stack)))


print(solution("1231234", 3))
