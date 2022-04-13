#바이러스
from collections import deque, defaultdict

computer_num = int(input())
network_num = int(input())
network_list = [list(map(int, input().split())) for _ in range(network_num)]
    
map = defaultdict(list)
for c1, c2 in network_list:
    map[c1].append(c2)
    map[c2].append(c1)

cnt = 0    
queue = deque([1])
visited = [False] * computer_num
while queue:
    cur = queue.popleft()
    visited[cur - 1] = True
    for v in map[cur]:
        if visited[v - 1] == False:
            queue.append(v)

print(visited.count(True) - 1)