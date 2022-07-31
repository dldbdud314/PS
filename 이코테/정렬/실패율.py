#프로그래머스
def solution(n, stages):
    count = [0] * (n + 2)
    for x in stages:
        count[x] += 1
    total = len(stages)
    fail_rate = []
    for i in range(1, n + 1):
        if total == 0: #분모가 0이 되는 경우 주의 (=스테이지에 도달한 유저가 없는 경우에 해당)
            fail_rate.append([0, i])
            continue
        fail_rate.append([count[i]/total, i])
        total -= count[i]
    fail_rate.sort(key=lambda x:(-x[0], x[1]))
    return list(map(lambda x:x[1], fail_rate))

print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
print(solution(4, [4, 4, 4, 4, 4]))
