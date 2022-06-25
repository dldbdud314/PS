from itertools import combinations

def solution(relation):
    keys = []
    cols = [k for k in range(len(relation[0]))]
    for i in range(1, len(cols)+1):
        for c in combinations(cols, i): #c: 칼럼 인덱스의 조합
            check = set()
            for row in relation:
                check.add(tuple(row[idx] for idx in c))
            if len(relation) == len(check):
                keys.append(c)
    #부분집합 검사해서 요소 제거
    flag = [True]*len(keys)
    for i in range(len(keys)):
        for j in range(i+1, len(keys)):
            if flag[i] and set(keys[i]) < set(keys[j]): flag[j] = False
    return flag.count(True)
    
print(solution([["a","1","aaa","c","ng"], ["a","1","bbb","e","g"], ["c","1","aaa","d","ng"], ["d","2","bbb","d","ng"]]))