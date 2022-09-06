# 1. 딕셔너리 이용
# 합계: 68.5 / 100.0 (효율성 3/5)
def solution1(words, queries):
    dictionary = dict()
    for word in words:
        for i in range(1, len(word) - 1): #접두사, 접미사 dictionary 저장
            f = word[0:i] + '?' * (len(word) - i)
            e = '?' * (len(word) - i) + word[-i:]
            if f in dictionary: 
                dictionary[f] += 1
            else: 
                dictionary[f] = 1
            if e in dictionary: 
                dictionary[e] += 1
            else: 
                dictionary[e] = 1
        t = '?' * len(word)
        if t in dictionary: dictionary[t] += 1
        else: dictionary[t] = 1
    ans = []
    for query in queries:
        if query in dictionary:
            ans.append(dictionary[query])
        else:
            ans.append(0)
    return ans

# 2. 트라이 활용
# 합계: 85.0 / 100.0 (효율성 4/5)
import sys
sys.setrecursionlimit(100001)
from collections import defaultdict

def build_trie(words, trie):
    for word in words:
        cur_root = trie
        for c in word:
            if not c in cur_root:
                cur_root[c] = {}
            cur_root = cur_root[c]
        cur_root['*'] = word
    return trie

def dfs(cur_root, depth, res, qlen):
    if depth > qlen:
        return
    for k, v in cur_root.items():
        if k == '*':
            if depth == qlen:
                res.append(v)
            continue
        dfs(v, depth + 1, res, qlen)

def search_dfs(trie, query):
    root_dict = trie
    res = []
    depth = 0
    for c in query:
        if c != '?':
            if c not in root_dict:
                return []
            root_dict = root_dict[c]
            depth += 1
        else:
            dfs(root_dict, depth, res, len(query))
            break
    return res

def word_lengths(words):
    lengths = defaultdict(int)
    for word in words:
        lengths[len(word)] += 1
    return lengths

def solution2(words, queries):
    front_trie = build_trie(words, {})
    end_trie = build_trie(list(map(lambda word: word[::-1], words)), {})
    lengths = word_lengths(words)
    res = []
    for query in queries:
        if query.count('?') == len(query): #전부 다 ?인 경우
            res.append(lengths[len(query)])
        else:
            c = 0
            if query[0] == '?':
                c = search_dfs(end_trie, query[::-1])
            else:
                c = search_dfs(front_trie, query)
            res.append(len(c))
    return res
    
print(solution2(["frodo", "front", "frost", "frozen", "frame", "kakao"], ["fro??", "????o", "fr???", "fro???", "pro?"]))