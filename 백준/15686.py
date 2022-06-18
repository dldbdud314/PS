#치킨거리
from itertools import combinations

def solution(n, m, city_map):
    houses, chickens = [], []
    for i in range(n):
        for j in range(n):
            if city_map[i][j] == 1: houses.append([i, j])
            elif city_map[i][j] == 2: chickens.append([i, j])
    min_total = float('inf')
    for x in combinations(chickens, m):
        total = 0
        for house in houses:
            chicken_dist = []
            for xx in x:
                chicken_dist.append((abs(house[0]-xx[0])+abs(house[1]-xx[1])))
            total += min(chicken_dist)
        min_total = min(total, min_total)
    return min_total

n, m = map(int, input().split())
city_map = [list(map(int, input().split())) for _ in range(n)]
print(solution(n, m, city_map))