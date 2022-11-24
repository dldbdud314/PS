# 줄 세우기
from collections import deque

n, m = map(int, input().split())
ans = []

# topological sort
adj_lst = {k: {'incoming': 0, 'dest': list()} for k in range(1, n + 1)}
for _ in range(m):
    a, b = map(int, input().split())
    adj_lst[a]['dest'].append(b)
    adj_lst[b]['incoming'] += 1

# find sources
sources = []
for node in adj_lst.keys():
    if adj_lst[node]['incoming'] == 0:
        sources.append(node)

# bfs
queue = deque(sources)
while queue:
    cur = queue.popleft()
    ans.append(cur)

    for d in adj_lst[cur]['dest']:
        adj_lst[d]['incoming'] -= 1
        if adj_lst[d]['incoming'] == 0:
            queue.append(d)

for x in ans:
    print(x, end=' ')
