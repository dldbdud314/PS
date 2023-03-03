"""
1655. 가운데를 말해요
** 삽입 정렬 && 이분 탐색 활용 --> 오 시간 초과...
"""
from bisect import insort_left

n = int(input())
sorted_arr = []
for idx in range(n):
    num = int(input())
    insort_left(sorted_arr, num)
    print(sorted_arr[(idx + 1) // 2]) if (idx + 1) % 2 == 1 else print(sorted_arr[idx // 2])
