#괄호의값
bracket_str = input()

def get_bracket_val(string):
    stack = []
    bracket_val = 0
    
    for b in string:
        if b == '(' or b == '[':
            stack.append(b)
        else:
            if not stack: return 0
            if b == ')':
                if stack[-1] == '(':
                    stack.pop()
                    stack.append('2')
                elif stack[-1] == '[': return 0
                elif stack[-1].isdigit(): 
                    total = 0
                    while stack and stack[-1].isdigit():
                        total += int(stack.pop())
                    if not stack: return 0
                    if stack[-1] == '(':
                        stack.pop()
                        push_val = total * 2
                        stack.append(str(push_val))
                    elif stack[-1] == '[': return 0
            else: #b == ']'
                if stack[-1] == '[':
                    stack.pop()
                    stack.append('3')
                elif stack[-1] == '(': return 0
                elif stack[-1].isdigit(): 
                    total = 0
                    while stack and stack[-1].isdigit():
                        total += int(stack.pop())
                    if not stack: return 0
                    if stack[-1] == '[':
                        stack.pop()
                        push_val = total * 3
                        stack.append(str(push_val))
                    elif stack[-1] == '(': return 0
    
    for x in stack:
        if x.isdigit(): bracket_val += int(x)
        else: return 0
        
    return bracket_val

print(get_bracket_val(bracket_str))

#my solution: 계산 결과와 괄호를 하나의 스택으로 처리
#아쉬운 점: 복잡하고 고려해야 할 케이스가 많다! 반례 추가하고 거르기 위해 계속 조건 추가하는 걸 서너번 반복,, 더 나은 풀이가 있을 거 같다,,