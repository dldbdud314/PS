def solution(routes):
    routes.sort(key = lambda x : (x[1], x[0]))
    cur = 0
    i = cur + 1
    cnt = 0
    while i < len(routes):
        if routes[cur][1] < routes[i][0]:
            cnt += 1
            cur = i
        i += 1
    return cnt + 1