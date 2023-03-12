
def dynamic_programming(matrix):  # dp 수행
    max_gold = 0
    for j in range(1, m):
        for i in range(n):
            matrix[i][j] = max(matrix[i-1][j-1] if i - 1 >= 0 else 0, matrix[i][j-1], matrix[i+1][j-1] if i + 1 < n else 0) + matrix[i][j]
            max_gold = max(matrix[i][-1], max_gold)

    return max_gold


# 입력부
T = int(input())
for _ in range(T):
    n, m = map(int, input().split())
    tmp = list(map(int, input().split()))
    matrix = []
    for i in range(0, len(tmp), m):
        matrix.append(tmp[i: i + m])

    print(dynamic_programming(matrix))
