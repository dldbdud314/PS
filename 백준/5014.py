#스타트링크
from collections import deque

def solution(F, S, G, U, D):
    queue = deque([(S, 0)])
    visited = [False] * F
    visited[S-1] = True
    while queue:
        floor, cnt = queue.popleft()
        if floor == G:
            return cnt
        if floor + U <= F and not visited[floor+U-1]:
            visited[floor+U-1] = True
            queue.append((floor + U, cnt + 1))
        if floor - D > 0 and not visited[floor-D-1]:
            visited[floor-D-1] = True
            queue.append((floor - D, cnt + 1))
    return "use the stairs"

F, S, G, U, D = map(int, input().split())
print(solution(F, S, G, U, D))