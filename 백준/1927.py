# 최소 힙
from heapq import heappop, heappush
import sys
input = sys.stdin.readline

n = int(input())
cmds = []
for _ in range(n):
    cmds.append(int(input()))

heap = []
for cmd in cmds:
    if cmd == 0:
        if heap:
            print(heappop(heap))
        else:
            print(0)
    else:
        heappush(heap, cmd)