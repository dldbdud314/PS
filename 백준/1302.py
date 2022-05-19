#베스트셀러

from collections import Counter

n = int(input())
books = [input() for _ in range(n)]

print(sorted(Counter(books).most_common(), key = lambda x:(-x[1], x[0]))[0][0])