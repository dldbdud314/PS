#A->B
from collections import deque

def getLeastCalc(start, target):
    queue = deque([(start, 0)])
    while queue:
        num, level = queue.popleft()
        if num == target:
            return level + 1
        if num < target:
            level += 1
            queue.append((num*2, level))
            queue.append((int(str(num)+'1'), level))
    return -1

a, b = map(int, input().split())
print(getLeastCalc(a,b))