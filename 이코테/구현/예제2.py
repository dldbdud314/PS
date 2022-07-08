#시각
def solution(n):
    cnt = 0
    for hour in range(n + 1):
        for min in range(60):
            for sec in range(60):
                if '3' in str(sec) or '3' in str(min) or '3' in str(hour):
                    cnt += 1
    return cnt

n = int(input())
print(solution(n))