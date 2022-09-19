def solution(n, words):
    word_set = set()
    turn = 1
    counts = [0] * (n + 1)
    ll = words[0][0]
    for word in words:
        counts[turn] += 1
        if word in word_set or ll != word[0]:
            return [turn, counts[turn]]
        else:
            word_set.add(word)
        if turn + 1 <= n:
            turn += 1
        else:
            turn = 1
        ll = word[-1]
    return [0, 0]