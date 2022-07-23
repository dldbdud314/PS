#로봇청소기
def turn_left(d):
    return {0 : 3, 3 : 2, 2 : 1, 1 : 0}.get(d)

def forward(d): #현재 방향에 대하여 앞 +1
    return {0 : (-1, 0), 1 : (0, 1), 2 : (1, 0), 3 : (0, -1)}.get(d)

def backward(d): #현재 방향에 대하여 뒤 +1
    return {0 : (1, 0), 1 : (0, -1), 2 : (-1, 0), 3 : (0, 1)}.get(d)

def solution(n, m, r, c, d, space):
    cleaned = [[False] * m for _ in range(n)]
    cnt = 0
    while True:
        if cnt == 4:
            dr, dc = backward(d)
            if space[r+dr][c+dc] == 1: #벽인 경우 끝
                break
            r, c = r + dr, c + dc #이동
            cnt = 0
        cleaned[r][c] = True #현재 칸 청소
        d = turn_left(d)
        dr, dc = forward(d)
        if not cleaned[r+dr][c+dc] and space[r+dr][c+dc] == 0:
            r, c = r + dr, c + dc #이동
            cnt = 0
        else:
            cnt += 1
    ans = 0
    for i in range(n):
        ans += cleaned[i].count(True)
    return ans

n, m = map(int, input().split())
r, c, d = map(int, input().split())
space = [list(map(int, input().split())) for _ in range(n)]
print(solution(n, m, r, c, d, space))