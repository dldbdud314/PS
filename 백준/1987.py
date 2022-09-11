#알파벳 - pypy3 시간초과
alphabets = {chr(i+65) : False for i in range(26)}
biggest = -float('inf')

r, c = map(int, input().split())
arr = [input() for _ in range(r)]
visited = [[False] * c for _ in range(r)]

def dfs(x, y, r, c, arr, cnt):
    global biggest, alphabets, visited
    visited[x][y] = True
    alphabets[arr[x][y]] = True
    biggest = max(biggest, cnt)
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    for dx, dy in dirs:
        if 0 <= x + dx < r and 0 <= y + dy < c and not visited[x+dx][y+dy] and not alphabets[arr[x+dx][y+dy]]:
            dfs(x + dx, y + dy, r, c, arr, cnt + 1)
    visited[x][y] = False
    alphabets[arr[x][y]] = False

dfs(0, 0, r, c, arr, 1)
print(biggest)