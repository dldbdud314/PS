#효율성 3번 웨 시간 초과....
from bisect import bisect_left, bisect_right
from collections import defaultdict

def count_by_range(arr, l, r): #'?' 이전의 query 탐색 범위 지정
    left = bisect_left(arr, l)
    right = bisect_right(arr, r)
    return right - left

def make_dictionary(words):
    dictionary, reversed_dictionary = defaultdict(list), defaultdict(list)
    for word in words:
        dictionary[len(word)].append(word)
        reversed_dictionary[len(word)].append(word[::-1])
    for k in dictionary.keys(): #사전순 정렬
        dictionary[k].sort()
        reversed_dictionary[k].sort()
    return dictionary, reversed_dictionary
    
def solution(words, queries):
    #단어 길이 별 나누기
    word_dict, word_dict_rev = make_dictionary(words)
    res = []
    for query in queries:
        qlen = len(query)
        if qlen not in word_dict:
            res.append(0)
            continue
        if query.count('?') == qlen:
            res.append(word_dict[qlen])
            continue
        cnt = 0
        if query[0] == '?':
            search_lst = word_dict_rev[qlen]
            cnt = count_by_range(search_lst, query[::-1].replace('?', 'a'), query[::-1].replace('?', 'z'))
        else:
            search_lst = word_dict[qlen]
            cnt = count_by_range(search_lst, query.replace('?', 'a'), query.replace('?', 'z'))
        res.append(cnt)
    return res
    
print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"], ["fro??", "????o", "fr???", "fro???", "pro?"]))