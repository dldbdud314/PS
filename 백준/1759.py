'''
암호 만들기: DFS
'''
res = []


def check_count(word):
    cnt = 0
    for x in word:
        if x in {'a', 'e', 'i', 'o', 'u'}:
            cnt += 1
    if cnt >= 1 and l - cnt >= 2:
        return True
    return False


def dfs(idx, depth, word):
    if depth == l:
        if check_count(word):  # 자음/모음 조건 충족 여부 확인
            global res
            res.append(word)
            return

    for k in range(idx, c):
        dfs(k + 1, depth + 1, word + letters[k])


l, c = map(int, input().split())
letters = list(input().split())
letters.sort()

dfs(0, 0, '')

print(res)