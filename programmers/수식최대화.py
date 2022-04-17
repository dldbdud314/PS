from itertools import permutations

def calculate(op1, op2, exp):
    if exp == '-':
        return op1 - op2
    elif exp == '+':
        return op1 + op2
    elif exp == '*':
        return op1 * op2

def solution(expression):
    #1. 연산자, 피연산자 배열에 저장
    operand = [] #피연산자
    operator = [] #연산자
    digit = ''
    for c in expression:
        if c.isdigit(): 
            digit += c
        else:
            operand.append(int(digit))
            digit = ''
            operator.append(c)
    operand.append(int(digit))
    
    #2. 연산자 순위 정하기 (순열)
    operator_orders = list(permutations(list(set(operator))))
    
    #3. 각 순위별 연산 작업
    results = []
    for order in operator_orders:
        for op in order:
            operand_copy = operand
            operator_copy = operator
            while op in operator:
                idx = operator.index(op)
                res = calculate(operand_copy[idx], operand_copy[idx+1], operator_copy[idx])
                operand_copy.pop(idx)
                operand_copy.pop(idx)
                operator_copy.pop(idx)
                operand_copy.insert(idx, res)
        results.append(abs(operand_copy[0]))
    
    return max(results)
    
print(solution("100-200*300-500+20"))

#구린_풀이