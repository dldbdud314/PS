from collections import defaultdict

#강의 풀이 참고
def solution(tickets):
    routes = defaultdict(list)
    for a, b in tickets:
        routes[a].append(b)
    for key in routes.keys():
        routes[key].sort(reverse=True)
    stack = ["ICN"]
    path = []
    while len(stack) > 0:
        top = stack[-1]
        if top not in routes or not routes[top]:
            path.append(stack.pop())
        else:
            stack.append(routes[top][-1])
            routes[top].pop()
    return path[::-1]

print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))