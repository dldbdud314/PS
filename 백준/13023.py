import sys

input = sys.stdin.readline

sys.setrecursionlimit(10 ** 5)

n, m = map(int, input().split())
friends = [list() for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    friends[a].append(b)
    friends[b].append(a)


def dfs(cur, depth, vis):
    if depth == 0:
        return True

    for nxt in friends[cur]:
        if not vis[nxt]:
            vis[nxt] = True
            if dfs(nxt, depth - 1, vis):
                return True
            vis[nxt] = False

    return False


res = 0
visited = [False] * n
for k in range(n):
    visited[k] = True
    if dfs(k, 4, visited):
        res = 1
        break
    visited[k] = False

print(res)