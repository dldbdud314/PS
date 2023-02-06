'''
DFS 재귀  -> 풀이 참고
'''
cnt, res = 0, 0


def dfs(cur_w, word):
    global cnt, res

    if len(cur_w) > 5:  # 종료 조건
        return

    if cur_w == word:
        res = cnt
        return

    cnt += 1  # 호출 횟수 ++

    for x in "AEIOU":
        dfs(cur_w + x, word)  # 덧붙이기


def solution(word):
    dfs('', word)
    return res


print(solution("AAAE"))

# 함수 호출 스택 이해할 것
