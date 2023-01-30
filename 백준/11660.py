# 구간 합 구하기 5 - Pypy 통과
n, m = map(int, input().split())
MAP = []
for _ in range(n):
    MAP.append(list(map(int, input().split())))

# 각각의 row 별 구간 합 연산해서 캐싱
sums = [[0] for _ in range(n)]  # 구간 합
for i in range(n):
    total = 0
    for j in range(n):
        total += MAP[i][j]
        sums[i].append(total)

# 쿼리 입력 받아서 구간 합 연산하기
res = []
for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    total = 0
    for i in range(x1 - 1, x2):
        total += (sums[i][y2] - sums[i][y1 - 1])
    res.append(total)

print(*res, sep='\n')
