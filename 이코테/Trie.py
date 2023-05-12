"""
Trie 베이스 코드: dict, dfs 활용
"""
from pprint import pprint

# tc
words = ["cat", "cats", "dog", "dogs", "app", "apple", "application"]
target = "app"  # expected output: ["app", "apple", "application"]

# build trie
trie = {}
for word in words:
    cur_root = trie
    for c in word:
        if c not in cur_root:
            cur_root[c] = {}
        cur_root = cur_root[c]
    cur_root['*'] = word

pprint(trie)


def dfs(cur):  # target에 대하여 가능한 모든 후보 리스트 (dfs search)
    for k, v in cur.items():
        if k == '*':
            res.append(v)
            continue
        dfs(v)


# search dfs
res = []
cur_root = trie
for c in target:
    cur_root = cur_root[c]
dfs(cur_root)  # 하위 탐색

print(res)
