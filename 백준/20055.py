"""
20055. 컨베이어 벨트 위의 로봇

** 시뮬레이션 (큐 활용)
자료구조: 컨베이어 벨트, 로봇 -> 큐
- 한칸 회전 : conveyer queue, robots rotate, robots 마지막 원소 drop
- 로봇 가능하면 한칸 이동, 역시 마지막 원소 drop
- 첫번째 칸 로봇 올리기
"""
from collections import deque

n, k = map(int, input().split())
conveyer_queue = deque(list(map(int, input().split())))
robots = deque([False] * n)  # 로봇 유무 큐

step = 1
while True:
    # 회전
    conveyer_queue.rotate(1)
    robots.rotate(1)
    robots[-1] = False  # 마지막 robot drop

    # 로봇 이동
    for i in range(n - 2, -1, -1):
        if robots[i] and not robots[i + 1] and conveyer_queue[i + 1] >= 1:
            robots[i + 1] = True
            robots[i] = False
            conveyer_queue[i + 1] -= 1
    robots[-1] = False  # 마지막 robot drop

    # 로봇 새로 올리기
    if conveyer_queue[0] > 0:
        conveyer_queue[0] -= 1
        robots[0] = True

    if conveyer_queue.count(0) >= k:
        break

    step += 1

print(step)
