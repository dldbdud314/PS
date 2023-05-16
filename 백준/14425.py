"""
14425. 문자열 집합
1. Trie
"""
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
trie = dict()


# trie에 단어 하나씩 적재
def store(word):
    cur_root = trie
    for c in word:
        if c not in cur_root:
            cur_root[c] = {}
        cur_root = cur_root[c]
    cur_root['*'] = word


# trie에 target 문자열 존재하는지 확인
def search(target):
    cur_root = trie
    for c in target:
        if c not in cur_root:
            return 0
        cur_root = cur_root[c]
    return 1 if '*' in cur_root and cur_root['*'] == target else 0


# make Trie
for _ in range(n):
    store(input())

total = 0
# target search
for _ in range(m):
    total += search(input())

print(total)

"""
2. Set 활용
"""

n1, m1 = map(int, input().split())
wsets = set([input() for _ in range(n1)])

total1 = 0
for _ in range(m1):
    target = input()
    total1 += int(target in wsets)

print(total1)

# 훨씬 시간+공간 효율적 -> 문자열 최대 길이 때문인듯 (500)
