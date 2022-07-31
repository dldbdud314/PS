#백준 18310
#sort -> 중간값
def solution(n, houses):
    houses.sort()
    return houses[n//2 if n % 2 == 1 else n//2 - 1]
n = int(input())
houses = list(map(int, input().split()))
print(solution(n, houses))

#초기 접근: set으로 중복을 제거한 뒤 중간값을 구했는데, 직접 해보니 거리의 총합이 최소라는 게 보장이 안됨