#연산자 끼워넣기
from itertools import permutations

def make_expression_list(exp):
    lst = []
    if exp[0] > 0:
        lst.extend(['+'] * exp[0])
    if exp[1] > 0:
        lst.extend(['-'] * exp[1])
    if exp[2] > 0:
        lst.extend(['*'] * exp[2])
    if exp[3] > 0:
        lst.extend(['%'] * exp[3])
    return lst

def calculate(op1, op2, exp):
    if exp == '+': return op1 + op2
    elif exp == '-': return op1 - op2
    elif exp == '*': return op1 * op2
    else: #문제 잘 읽기!!
        if op1 >= 0: return op1 // op2
        else: return -(abs(op1) // op2)

n = int(input())
nums = list(map(int, input().split()))
exp = list(map(int, input().split()))

exp_lst = make_expression_list(exp)
orders = list(set(permutations(exp_lst)))

min_res = float('inf')
max_res = -float('inf')
for order in orders:
    res = nums[0]
    for i in range(len(order)):
        res = calculate(res, nums[i+1], order[i])
    max_res = max(max_res, res)
    min_res = min(min_res, res)

print(max_res)
print(min_res)