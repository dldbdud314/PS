from collections import deque


def valid_word(word1, word2):
    total = len(word1)
    cnt = 0
    for c1, c2 in zip(word1, word2):
        if c1 == c2:
            cnt += 1
    if (total - 1) == cnt:
        return True
    return False


def solution(begin, target, words):
    visited = {word: False for word in words}
    queue = deque([(begin, 0)])
    while queue:
        word, level = queue.popleft()

        if word == target:
            return level

        if word != begin:
            visited[word] = True

        for w in words:
            if valid_word(w, word) and not visited[w]:
                queue.append((w, level + 1))

    return 0