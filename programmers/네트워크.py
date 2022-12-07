def dfs(x, n, computers, visited):
    visited[x] = True

    for y in range(n):
        if y == x:
            continue
        if computers[x][y] == 1 and not visited[y]:
            dfs(y, n, computers, visited)


def solution(n, computers):
    visited = [False] * n

    count = 0
    for x in range(n):
        if not visited[x]:
            dfs(x, n, computers, visited)
            count += 1

    return count