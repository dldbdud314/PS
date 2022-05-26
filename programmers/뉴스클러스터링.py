from collections import Counter
import math

def solution(str1, str2):
    #1. 두개의 문자 집합 전처리해서 만들기
    str1_lst, str2_lst = list(), list()
    for i in range(len(str1) - 1):
        if str1[i:i+2].isalpha():
            str1_lst.append(str1[i:i+2].lower())
    for i in range(len(str2) - 1):
        if str2[i:i+2].isalpha():
            str2_lst.append(str2[i:i+2].lower())
    
    if not str1_lst and not str2_lst: #공집합인 경우
        return 1 * 65536
    
    #2. 교집합, 합집합 만들어서 자카드 유사도 구하기
    str1_set = Counter(str1_lst)
    str2_set = Counter(str2_lst)
    a = str1_set & str2_set #교집합
    b = str1_set | str2_set #합집합
    return math.trunc(sum(a.values())/sum(b.values())*65536)