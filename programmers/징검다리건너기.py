def solution(stones, k):
    l, r = 1, max(stones)
    res = 1

    while l <= r:
        mid = (l + r) // 2  # 건너는 친구 수 
        # mid명 건넌다고 가정했을 때 연속 점프수 -> k 초과 시 건너기 불가능하다고 판단하고 break
        cnt = 0
        for stone in stones:
            if stone - mid < 0:
                cnt += 1
                if cnt >= k:
                    r = mid - 1  # 건널 수 없음 -> 건널 사람 줄이기
                    break
            else:
                cnt = 0
        else:  # break없이 loop 무사 탈출 -> mid명 건널 수 있음 -> 건널 사람 늘리기
            res = mid
            l = mid + 1

    return res