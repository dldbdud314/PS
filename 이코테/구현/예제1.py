#상하좌우
def get_dir(d): #(dx, dy)
    return {'L' : (0, -1), 'R' : (0, 1), 'U' : (-1, 0), 'D' : (1, 0)}.get(d)

def solution(n, dirs):
    x, y = 0, 0
    for dir in dirs:
        dx, dy = get_dir(dir)
        if 0 <= x + dx < n and 0 <= y + dy < n:
            x += dx
            y += dy
        print(x, y)
    return x + 1, y + 1

n = int(input())
dirs = list(input().split())
print(solution(n, dirs))