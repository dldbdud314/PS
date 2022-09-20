def solution(skill, skill_trees):
    graph = dict()
    for i in range(1, len(skill)):
        first, sec = skill[i-1], skill[i]
        graph[sec] = first
    cnt = 0
    for skills in skill_trees:
        visited = {node : False for node in skill}
        for x in skills:
            if x not in graph:
                visited[x] = True
            else:
                todo = graph[x] #선행노드
                if not visited[todo]: #선행노드를 방문하지 않았으면 성립 X
                    break
                else:
                    visited[x] = True
        else: 
            cnt += 1
    return cnt

print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))