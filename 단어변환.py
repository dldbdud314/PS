from collections import deque

def check_word(w1, w2):
    cnt = 0
    for x1, x2 in zip(w1, w2):
        if x1 == x2: cnt += 1
    if cnt == len(w1)-1:
        return True
    else:
        return False

def solution(begin, target, words):
    if target not in words:
        return 0
    
    ans = 0
    queue = deque([(begin, 0)])
    visited = {key : False for key in words}
    while queue:
        cur = queue.popleft()
        if cur[0] == target:
            ans = cur[1] #현재 레벨 저장
            break
        for w in words:
            if visited[w] == False and check_word(cur[0], w):
                queue.append((w, cur[1] + 1))
                visited[w] = True
    return ans