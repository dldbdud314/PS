def solution(rows, columns, queries):
    arr = [[0] * columns for _ in range(rows)]
    num = 1
    for i in range(rows):
        for j in range(columns):
            arr[i][j] = num
            num += 1
    ans = []
    for x1, y1, x2, y2 in queries:
        save = arr[x1-1][y1-1]
        smallest = save
        for i in range(x1, x2):
            arr[i-1][y1-1] = arr[i][y1-1]
            smallest = min(arr[i-1][y1-1], smallest)
        for j in range(y1, y2):
            arr[x2-1][j-1] = arr[x2-1][j]
            smallest = min(arr[x2-1][j-1], smallest)
        for i in range(x2 - 1, x1 - 1, -1):
            arr[i][y2-1] = arr[i-1][y2-1]
            smallest = min(arr[i][y2-1], smallest)
        for j in range(y2 - 1, y1, -1):
            arr[x1-1][j] = arr[x1-1][j-1]
            smallest = min(arr[x1-1][j], smallest)
        arr[x1-1][y1] = save
        ans.append(smallest)
    return ans
