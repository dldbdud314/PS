from itertools import product
from collections import defaultdict
from bisect import bisect_left

def make_dictionary(info):
    dictionary = defaultdict(list)
    for x in info:
        for p in product([x[0], "-"], [x[1], "-"], [x[2], "-"], [x[3], "-"]):
            dictionary[p].append(int(x[4]))
    #선소팅
    for _, val in dictionary.items():
        val.sort()
    return dictionary

def solution(info, query):
    info = [a.split() for a in info]
    dictionary = make_dictionary(info)
    #list가 길수도 -> 빠른 탐색 방법 필요 (이분탐색)
    result = []
    for q in query:
        l, _, p, _, c, _, f, point = q.split()
        idx = bisect_left(dictionary[(l, p, c, f)], int(point))
        result.append(len(dictionary[(l, p, c, f)]) - idx)
        
    return result
    
print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"], ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))

#이분탐색 변형: X보다 작은, 가장 가까운 index 찾는 게 목표
# def binary_search(arr, target):
#     l = 0
#     r = len(arr) - 1
#     idx = float('inf')
#     while l <= r:
#         mid = (l+r) // 2
#         if arr[mid] >= target and mid < idx: #idx 갱신용
#             idx = mid
#         if arr[mid] > target:
#             r = mid - 1
#         else:
#             l = mid + 1
#     return len(arr) - idx

# bisect를 사용하면 되는 거였다...(하얀별)