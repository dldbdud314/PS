"""
17298. 오큰수
** Stack
"""
n = int(input())
arr = list(map(int, input().split()))

res = [-1] * n

stack = [0]
for idx in range(1, n):
    while stack and arr[stack[-1]] < arr[idx]:
        res[stack.pop()] = arr[idx]
    stack.append(idx)

print(*res)
