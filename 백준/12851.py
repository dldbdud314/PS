#숨바꼭질2
from collections import deque, defaultdict

def get_shortest_time_and_cnt(start, target):
    #edge case
    if start == target:
        return 0, 1
    if start > target:
        return start - target, 1
    
    queue = deque([(start, 0)])
    visited = [False] * 100001
    counter = defaultdict(int)
    while queue:
        pos, level = queue.popleft()
        visited[pos] = True
        if pos == target:
            counter[level] += 1
        else:
            for npos in [pos - 1, pos + 1, pos * 2]:
                if 0 <= npos <= target + 1 and not visited[npos]:
                    queue.append((npos, level + 1))
                    
    min_key = min(counter.keys())
    return min_key, counter[min_key]

n, k = map(int, input().split())
time, cnt = get_shortest_time_and_cnt(n, k)
print(time)
print(cnt)