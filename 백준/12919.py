#A와 B 2
from collections import deque

s = input()
t = input()

queue = deque([s])
flag = False

while queue:
    cur = queue.popleft()
    if cur == t:
        flag = True
        break
    if len(cur) > len(t):
        break
    for x in [cur + 'A', (cur + 'B')[::-1]]:
        if x in t or x in t[::-1]:
            queue.append(x)
    
print(1) if flag else print(0)