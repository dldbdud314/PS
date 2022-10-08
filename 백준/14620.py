#꽃길
from itertools import combinations

n = int(input())
garden = [list(map(int, input().split())) for _ in range(n)]

pos = []
for i in range(1, n - 1):
    for j in range(1, n - 1):
        tmp = [(i, j), (i-1, j), (i, j+1), (i+1, j), (i, j-1)]
        pos.append(tmp)

least_cost = float('inf')
for p in combinations(pos, 3):
    taken = [[False] * n for _ in range(n)]
    flag = False
    cost = 0
    for pp in p:
        for i, j in pp:
            if taken[i][j]:
                flag = True
                break
            cost += garden[i][j]
            taken[i][j] = True
        if flag: break
    if not flag and least_cost > cost:
        least_cost = cost
        
print(least_cost)