from collections import deque

def make_graph(n, matrix):
    graph = dict()
    for i in range(n):
        graph[i] = []
        for j in range(i+1, n):
            if matrix[i][j] == 1:
                graph[i].append(j)
    return graph

def solution(n, computers):
    graph = make_graph(n, computers)
    cnt = 0
    visited = [False] * n
    for key in graph.keys():
        if visited[key] == False:
            queue = deque([key])
            while queue:
                cur = queue.popleft()
                if visited[cur] == False:
                    visited[cur] = True
                    for v in graph[cur]:
                        queue.append(v)
            cnt += 1
    return cnt

solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]])

#뭐지 무ㅓ가 잘못된걸까..