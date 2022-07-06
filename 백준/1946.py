#신입사원
import sys
def solution(lst, n):
    lst.sort()
    res = 1
    prev1, prev2 = lst[0][0], lst[0][1]
    for i in range(1, n):
        cur1, cur2 = lst[i]
        if cur2 < prev2:
            res += 1
            prev1, prev2 = cur1, cur2
    return res

T = int(input())
ans = []
for i in range(T):
    n = int(input())
    lst = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    ans.append(solution(lst, n))
for a in ans:
    print(a)