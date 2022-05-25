from collections import deque

def solution(priorities, location):
    priorities = [[x, False] for x in priorities]
    priorities[location][1] = True
    queue = deque(priorities)
    
    cnt = 1
    while queue:
        front = queue.popleft()
        flag = False
        for pri, _ in queue:
            if pri > front[0]: 
                queue.append(front)
                flag = True
                break
        if not flag: #자기자신이 제일 큼
            if front[1]: return cnt
            cnt += 1
    
print(solution([1, 1, 9, 1, 1, 1], 0))