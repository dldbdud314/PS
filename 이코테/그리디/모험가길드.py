#[1회차] 초기 접근 잘못하고 코드 구현 실패 - 풀이 참고
def solution(arr):
    arr.sort()
    res = 0
    cnt = 0 #현재 그룹의 인원 수
    for x in arr:
        cnt += 1
        if cnt >= x:
            res += 1 #그룹 결성
            cnt = 0
    return res

n = int(input())
arr = list(map(int, input().split()))
print(solution(arr))