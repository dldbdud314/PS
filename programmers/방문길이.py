def move(d):
    return {'U' : (1, 0), 'D' : (-1, 0), 'R' : (0, 1), 'L' : (0, -1)}.get(d)

def solution(dirs):
    cur_pos = (0, 0)
    visited = set()
    path = 0
    for dir in dirs:
        cx, cy = cur_pos
        dx, dy = move(dir)
        if -5 <= cx + dx <= 5 and -5 <= cy + dy <= 5:
            if ((cx, cy), (cx + dx, cy + dy)) not in visited:
                visited.add(((cx, cy), (cx + dx, cy + dy)))
                visited.add(((cx + dx, cy + dy), (cx, cy)))
                path += 1
            cur_pos = (cx + dx, cy + dy)

    return path