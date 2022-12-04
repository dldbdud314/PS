def is_nearby1(place, x, y):
    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    for dx, dy in dirs:
        if 0 <= x + dx < 5 and 0 <= y + dy < 5:
            if place[x + dx][y + dy] == 'P': # 거리 1
                return True
            if place[x + dx][y + dy] == 'O' and 0 <= x + dx * 2 < 5 and 0 <= y + dy * 2 < 5 and place[x + dx * 2][
                y + dy * 2] == 'P':  # 거리 2 (중간에 비었으며 + 두칸 건너 사람이 있는 경우)
                return True

    return False


def is_nearby2(place, x, y):
    dirs = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    for dx, dy in dirs:
        if 0 <= x + dx < 5 and 0 <= y + dy < 5 and place[x + dx][y + dy] == 'P':
            if place[x][y + dy] == 'O' or place[x + dx][y] == 'O':
                return True

    return False


def check_dis(place):
    for i in range(5):
        for j in range(5):
            if place[i][j] == 'P':
                # 1. 상하좌우 네방향 (거리 1 && 2 둘 다 체크하기!)
                if is_nearby1(place, i, j):
                    return 0
                # 2. 대각선 네방향
                if is_nearby2(place, i, j):
                    return 0
    return 1


def solution(places):
    res = []
    for place in places:
        res.append(check_dis(place))

    return res


print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
                ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
                ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))
