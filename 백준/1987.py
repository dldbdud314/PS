# 알파벳

r, c = map(int, input().split())
arr = [input() for _ in range(r)]
visited = [[False] * c for _ in range(r)]
alphabets = [False] * 26

longest = -float('inf')


def char_to_idx(x):
    return ord(x) - ord('A')


def dfs(i, j, d, visited, alphabets):
    visited[i][j] = True
    alphabets[char_to_idx(arr[i][j])] = True

    global longest
    longest = max(d, longest)

    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    for di, dj in dirs:
        if 0 <= i + di < r and 0 <= j + dj < c and not visited[i + di][j + dj] and not alphabets[char_to_idx(arr[i+di][j+dj])]:
            dfs(i + di, j + dj, d + 1, visited, alphabets)

    visited[i][j] = False
    alphabets[char_to_idx(arr[i][j])] = False


dfs(0, 0, 1, visited, alphabets)
print(longest)