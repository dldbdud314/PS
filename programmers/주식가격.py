from collections import deque

def solution(prices):
    ans = []
    queue = deque(prices)
    while queue:
        front = queue.popleft()
        idx = 1
        flag = False
        for val in queue:
            if val < front:
                ans.append(idx)
                flag = True
                break
            idx += 1
        if not flag:
            ans.append(len(queue))
    return ans

print(solution([1, 2, 3, 2, 3]))