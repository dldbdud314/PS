#경사로
def solution(n, l, roads):
    row_flags = [True] * n
    col_flags = [True] * n
    #가로 check
    for i in range(n):
        row_ramps = [False] * n
        for j in range(n-1):
            if roads[i][j] < roads[i][j+1]: #낮 -> 높
                if roads[i][j+1] - roads[i][j] > 1:
                    row_flags[i] = False
                    break
                if j - l + 1 < 0 or any(roads[i][k] != roads[i][j] for k in range(j-l+1, j)) or any(row_ramps[k] for k in range(j-l+1, j+1)):
                    row_flags[i] = False
                    break
                for k in range(j-l+1, j+1):
                    row_ramps[k] = True
            elif roads[i][j] > roads[i][j+1]: #높 -> 낮
                if roads[i][j] - roads[i][j+1] > 1:
                    row_flags[i] = False
                    break
                if j + l >= n or any(roads[i][k] != roads[i][j+1] for k in range(j+1, j+l+1)):
                    row_flags[i] = False
                    break
                for k in range(j+1, j+l+1):
                    row_ramps[k] = True
    #세로 check
    for j in range(n):
        col_ramps = [False] * n
        for i in range(n-1):
            if roads[i][j] < roads[i+1][j]: #낮 -> 높
                if roads[i+1][j] - roads[i][j] > 1:
                    col_flags[j] = False
                    break
                if i - l + 1 < 0 or any(roads[k][j] != roads[i][j] for k in range(i-l+1, i)) or any(col_ramps[k] for k in range(i-l+1, i+1)):
                    col_flags[j] = False
                    break
                for k in range(i-l+1, i+1):
                    col_ramps[k] = True
            elif roads[i][j] > roads[i+1][j]: #높 -> 낮
                if roads[i][j] - roads[i+1][j] > 1:
                    col_flags[j] = False
                    break
                if i + l >= n or any(roads[k][j] != roads[i+1][j] for k in range(i+1, i+l+1)):
                    col_flags[j] = False
                    break
                for k in range(i+1, i+l+1):
                    col_ramps[k] = True
    return row_flags.count(True) + col_flags.count(True)

n, l = map(int, input().split())
roads = [list(map(int, input().split())) for _ in range(n)]
print(solution(n, l, roads))