from collections import deque

def solution(people, limit):
    people.sort(reverse=True)
    queue = deque(people)
    cnt = 0 #구명보트 개수
    while queue:
        p = queue.popleft()
        r = queue.pop() if len(queue) > 0 else 0
        if (r+p) > limit:
            queue.append(r)
        cnt += 1
    return cnt
