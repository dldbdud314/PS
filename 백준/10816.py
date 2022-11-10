# 숫자 카드 2
import sys
from bisect import bisect_left, bisect_right


def count_by_range(num):
    return bisect_right(cards, num) - bisect_left(cards, num)


n = int(input())
cards = list(map(int, sys.stdin.readline().split()))
m = int(input())
numbers = list(map(int, sys.stdin.readline().split()))

cards.sort()
res = []
for number in numbers:
    print(count_by_range(number), end=' ')
