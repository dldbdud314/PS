#1. 단순 해시
#participant 돌면서 딕셔너리 저장 -> completion 돌면서 딕셔너리에서 하나씩 빼고 -> 1 이상인 요소 리턴
def solution1(participant, completion):
    d = {}
    for x in participant:
        d[x] = d.get(x, 0) + 1
    for x in completion:
        d[x] -= 1
    for k, v in d.items():
        if v > 0: return k

#2. Counter 활용
from collections import Counter    
def solution2(participant, completion):
    return list((Counter(participant)-Counter(completion)).keys())[0]