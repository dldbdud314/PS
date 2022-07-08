#무한루프
def turn_left(d):
    return {0 : 3, 1 : 0, 2 : 1, 3 : 2}.get(d)

def move_forward(d): #해당 방향으로 움직이기
    return {0 : (-1, 0), 1 : (0, 1), 2 : (1, 0), 3 : (0, -1)}.get(d)

def move_backward(d): #반대 방향으로 움직이기
    return {0 : (1, 0), 1 : (0, -1), 2 : (-1, 0), 3 : (0, 1)}.get(d)


def solution(game_map, n, m, y, x, d):
    visited = [[False] * m for _ in range(n)]
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    res = 1
    while True:
        #현재 위치에서 네 방향으로 갈수 있는지부터 check
        flag = False
        for dy, dx in dirs:
            if game_map[y+dy][x+dx] == 0 and not visited[y+dy][x+dx]:
                flag = True #하나라도 갈 수 있으면 True
                break
        if flag:
            d = turn_left(d)
            dy, dx = move_forward(d)
            if game_map[y+dy][x+dx] == 0 and not visited[y+dy][x+dx]:
                y += dy
                x += dx
                visited[y+dy][x+dx] = True
                res += 1
        else:
            dy, dx = move_backward(d)
            if game_map[y+dy][x+dx] == 1:
                break
            y += dy
            x += dx
    return res

n, m = map(int, input().split())
a, b, d = map(int, input().split())
game_map = [list(map(int, input().split())) for _ in range(n)]
print(solution(game_map, n, m, a, b, d))