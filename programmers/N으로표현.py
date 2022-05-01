from itertools import product

def operate(set1, set2):
    res = set()
    for x, y in product(list(set1), list(set2)):
        res.add(x + y)
        res.add(x - y)
        res.add(x * y)
        if y != 0: res.add(x // y)
    return res

def solution(N, number):
    if number == N: return 1 #edge case
    dp = [0] * 10
    dp[1] = {N}
    for i in range(1, 9):
        new_set = set()
        new_set.add(int(str(N)*(i+1))) #NNN.. 형태
        for j in range(1, i + 1):
            new_set.update(operate(dp[j], dp[i+1-j]))
        if number in new_set: return i + 1
        dp[i + 1] = new_set
    return -1

print(solution(2, 11))