def solution(x, y):
    dirs = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (-1, 2), (1, -2), (-1, -2)]
    cnt = 0
    for dx, dy in dirs:
        if 0 <= dx + x < 8 and 0 <= dy + y < 8:
            cnt += 1
    return cnt

pos = input()
x, y = ord(pos[0]) - ord('a'), int(pos[1])-1
print(solution(x, y))