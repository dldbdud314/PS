#백준 1715
from heapq import heappop, heappush

def solution(n, cards):
    res = 0
    while cards:
        a = heappop(cards)
        if cards: b = heappop(cards)
        else: break
        heappush(cards, a + b)
        res += (a + b)
    return res
n = int(input())
cards = []
for _ in range(n):
    heappush(cards, int(input()))
print(solution(n, cards))