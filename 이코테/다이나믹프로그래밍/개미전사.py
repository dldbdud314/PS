#정석
def solution(n, store):
    d = [0] * n
    d[0] = store[0]
    d[1] = store[1]
    for i in range(2, n):
        d[i] = max(d[i - 1], d[i - 2] + store[i])
    return d[n-1]

#my
def my_solution(n, store):
    d = [0] * n
    d[0] = store[0]
    d[1] = store[1]
    for i in range(2, n):
        d[i] = max(d[0 : i - 1]) + store[i]
    return max(d)

n = int(input())
store = list(map(int, input().split()))
print(solution(n, store))