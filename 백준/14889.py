#스타트와 링크
from itertools import combinations

def solution(n, matrix):
    c = list(combinations(range(n), n//2))
    smallest = float('inf')
    for i in range(len(c) // 2):
        start = c[i]
        link = c[len(c) - 1 - i]
        st = 0
        for x, y in combinations(start, 2):
            st += matrix[x][y]
            st += matrix[y][x]
        lt = 0
        for x, y in combinations(link, 2):
            lt += matrix[x][y]
            lt += matrix[y][x]
        smallest = min(smallest, abs(lt - st))
    return smallest

n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
print(solution(n, matrix))
