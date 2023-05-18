

def reassemble(c1, i1, org, prev):
    # 다음으로 큰 글자 찾고
    # 나머지 sorted 덧붙이고 return
    for c2 in prev:
        if c1 < c2:
            prev.remove(c2)
            res = list(org[:i1]) + [c2] + sorted(prev + [c1])
            return ''.join(res)


def biggerIsGreater(w):
    prev = []
    for i in range(len(w) - 1, -1, -1):
        # 더 큰 게 나올 때까지 앞으로 이동
        prev.sort()
        if not prev or prev[-1] <= w[i]:
            prev.append(w[i])
        else:
            return reassemble(w[i], i, w, prev)

    return "no answer"


for s in ["lmno", "dcba", "dcbb", "abdc", "abcd", "fedcbabcd"]:
    print(biggerIsGreater(s))
