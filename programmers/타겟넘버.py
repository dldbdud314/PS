from collections import deque

def solution(numbers, target):
    queue = deque([0])
    for n in range(len(numbers)):
        num = numbers[n]
        for _ in range(2**n):
            cur = queue.popleft()
            queue.append(cur - num)
            queue.append(cur + num)
    return queue.count(target)