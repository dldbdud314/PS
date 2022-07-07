#멀티탭스케쥴링
def solution(orders, n, k):
    plug = []
    res = 0
    for i in range(k):
        if orders[i] in plug:
            continue
        if len(plug) < n:
            plug.append(orders[i])
            continue
        note = [k-i] * n
        for m in range(n):
            flag = False #가장 빨리 등장할 때  break하기 위해
            for j in range(i, k):
                if orders[j] == plug[m]:
                    note[m] = j-i
                    flag = True
                    break
            if flag: continue
        biggest = -float('inf')
        idx = 0
        for m in range(n):
            if biggest < note[m]:
                biggest = note[m]
                idx = m
        plug[idx] = orders[i]
        res += 1
    return res

n, k = map(int, input().split())
orders = list(map(int, input().split()))
print(solution(orders, n, k))