# 단순 구현 -> 슬라이딩 윈도우로 효율성 개선

def solution(elements):
    l = len(elements)
    sums = set()
    for k in range(1, l + 1):
        s, e = 0, k - 1  # 시작/끝 인덱스
        cur_sum = sum(elements[s: e + 1])
        tmp = {cur_sum}
        for _ in range(l - 1):  # l회
            cur_sum -= elements[s]
            s += 1
            e = (e + 1) % l
            cur_sum += elements[e]
            tmp.add(cur_sum)
        sums.update(tmp)

    return len(sums)


print(solution([7, 9, 1, 1, 4]))
