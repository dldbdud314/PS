#파일정리
from collections import Counter

n = int(input())
files = []
for _ in range(n):
    s = input()
    _, file = s.split('.')
    files.append(file)
for word, cnt in sorted(Counter(files).items()):
    print(word, cnt, sep = ' ')