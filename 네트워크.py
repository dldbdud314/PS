def dfs(x, graph, visited):
    if visited[x] == True:
        return
    visited[x] = True
    for val in graph[x]:
        dfs(val, graph, visited)

def make_graph(n, matrix):
    graph = dict()
    for i in range(n):
        graph[i] = []
        for j in range(n):
            if i != j and matrix[i][j] == 1:
                graph[i].append(j)
    return graph

def solution(n, computers):
    graph = make_graph(n, computers)
    cnt = 0
    visited = [False] * n
    for x in graph:
        if visited[x] == False:
            dfs(x, graph, visited)
            cnt += 1
    return cnt