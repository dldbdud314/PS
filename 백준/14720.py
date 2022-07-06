#우유축제
def next(key):
    return {0 : 1, 1 : 2, 2 : 0}.get(key)

def solution(arr):
    find = 0
    res = 0
    for a in arr:
        if a == find:
            res += 1
            find = next(a)
    return res

n = int(input())
arr = list(map(int, input().split()))
print(solution(arr))