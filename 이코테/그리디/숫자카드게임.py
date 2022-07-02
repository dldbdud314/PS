def solution(n, m , cards):
    mins = []
    for card in cards:
        mins.append(min(card))
    return max(mins)

n, m = map(int, input().split())
cards = [list(map(int, input().split())) for _ in range(n)]
print(solution(n, m, cards))