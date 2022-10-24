from collections import deque
from itertools import permutations

n = int(input())
scv = list(map(int, input().split()))

queue = deque([(scv, 0)])

visited = set()  # 남아 있는 체력 check
visited.add(tuple(scv))

while queue:
    cur_scv, cnt = queue.popleft()

    if not cur_scv:
        print(cnt)
        break

    for x in permutations(cur_scv):
        x = list(x)
        try:
            x[0] = 0 if x[0] - 9 <= 0 else x[0] - 9
            x[1] = 0 if x[1] - 3 <= 0 else x[1] - 3
            x[2] = 0 if x[2] - 1 <= 0 else x[2] - 1
        except:
            pass

        new_x = []
        for xx in x:
            if xx > 0: new_x.append(xx)

        if tuple(new_x) not in visited:
            queue.append((new_x, cnt + 1))
            visited.add(tuple(new_x))