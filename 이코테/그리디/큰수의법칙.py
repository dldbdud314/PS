def solution(m, k, arr):
    arr.sort(reverse=True) #그리디
    total = 0 
    cnt = 0 #총 몇개 더했는지 -> m와 비교
    cur_cnt = 0 #현재 인덱스 몇개 -> k와 비교
    while cnt < m:
        if cur_cnt < k:
            total += arr[0]
            cur_cnt += 1
        else:
            total += arr[1]
            cur_cnt = 0
        cnt += 1
    return total

n, m, k = map(int, input().split())
arr = list(map(int, input().split()))
print(solution(m, k, arr))
