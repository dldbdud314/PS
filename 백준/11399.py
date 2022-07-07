#ATM
def solution(n, p):
    p.sort()
    total = 0
    sums = [0] * n
    for i in range(n):
        total += p[i]
        sums[i] = total
    return sum(sums)

n = int(input())
p = list(map(int, input().split()))
print(solution(n, p))