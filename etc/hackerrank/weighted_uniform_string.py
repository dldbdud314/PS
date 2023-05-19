from collections import defaultdict


def weightedUniformStrings(s, queries):
    # store alphabets and max counts
    tmps = s + '0'
    record, cur = defaultdict(int), defaultdict(int)
    cur[tmps[0]] = 1
    for i in range(1, len(tmps)):
        if tmps[i] != tmps[i - 1]:
            record[tmps[i - 1]] = max(record[tmps[i - 1]], cur[tmps[i - 1]])
            cur[tmps[i - 1]] = 0
        cur[tmps[i]] += 1

    # main logic
    res = []
    for query in queries:
        for c in record.keys():
            w = ord(c) - ord('a') + 1
            if query % w == 0 and query <= record[c] * w:
                res.append("Yes")
                break
        else:
            res.append("No")

    return res
