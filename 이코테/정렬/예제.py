#두 배열의 원소 교체
def solution(k, a, b):
    a.sort()
    b.sort(reverse = True)
    for i in range(k):
        if a[i] < b[i]:
            a[i], b[i] = b[i], a[i]
        else:
            break
    return sum(a)

n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
print(solution(k, a, b))