"""
2696. 중앙값 구하기

** 삽입 정렬
- 입출력이 까다로움.. ㄸㅔ잉;
- 단순 삽입 정렬 알고리즘 -> 시간 초과
- 최적화 : inline stable sort -> 이미 정렬된 새로운 배열에 원소 추가하기 (bisect의 insort 활용)
"""
import sys
from bisect import insort_left

input = sys.stdin.readline


def get_input_by_ten():  # 10개씩 입력 받기
    m = int(input())
    data = []
    if m % 10 == 0:
        for _ in range(m // 10):
            data.extend(list(map(int, input().split())))
    else:
        for _ in range(m // 10 + 1):
            data.extend(list(map(int, input().split())))
    return data


def print_by_ten(data):  # 10개씩 출력
    print(len(data))
    k = 0
    while k < len(data):
        if k > 1 and k % 10 == 0:
            print()
        print(data[k], end=' ')
        k += 1
    print()


T = int(input())
for _ in range(T):
    arr = get_input_by_ten()  # 입력부 (주의 !)
    cur_arr, res = [], []
    for i, x in enumerate(arr):
        # 삽입할 자리를 찾는 과정 -> bisect로 최적화 가능? -> 통과..
        insort_left(cur_arr, x)
        # for j in range(i, 0, -1):
        #     if arr[j] < arr[j - 1]:
        #         arr[j], arr[j - 1] = arr[j - 1], arr[j]  # swap
        #     else:
        #         break
        if (i + 1) % 2 == 1:  # 홀수번째인 경우
            res.append(cur_arr[(i + 1) // 2])  # 중앙값
    # 출력부 (주의 !)
    print_by_ten(res)
