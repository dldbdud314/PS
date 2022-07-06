#설탕배달
def solution(N):
    n = N // 5
    while n >= 0:
        if ((N - 5 * n) % 3) == 0:
            m = (N - 5 * n) // 3
            return m + n
        else:
            n -= 1
    return -1
    
n = int(input())
print(solution(n))