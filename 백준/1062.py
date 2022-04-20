#가르침
from collections import defaultdict

def get_max_count1(k, word_list):
    if k < 5: return 0
    
    dictionary = defaultdict(int)
    word_set_list = [set(x) for x in word_list]
    total_word_set = set()
    for word in word_list:
        total_word_set.update(word)
    total_word_list = list(total_word_set)
    for c in total_word_list:
        for word_set in word_set_list:
            if c in word_set: 
                dictionary[c] += 1
    sorted_dict = sorted(dictionary.items(), key = lambda x: x[1], reverse = True)
    k_set = set()
    idx = 0
    for key, _ in sorted_dict:
        if idx >= k: break
        k_set.add(key) 
        idx += 1
    cnt = 0
    for word_set in word_set_list:
        if word_set < k_set or word_set == k_set: cnt += 1
    
    return cnt

from itertools import combinations
#시간초과ㅠㅠ
def get_max_count2(k, word_list):
    if k < 5: return 0
    
    default_set = {'a', 'n', 't', 'i', 'c'}
    cropped_word_list = [word[4:-4] for word in word_list]
    word_set_list = [set(x) for x in cropped_word_list]
    word_set_list = [word_set - default_set for word_set in word_set_list]
    total_char_set = set()
    for word_set in word_set_list:
        total_char_set.update(word_set)
    total_char_list = list(total_char_set)
    m = k - 5
    if len(total_char_list) < k-5: m = len(total_char_list)
    max_cnt = -float('inf')
    for char_set in combinations(total_char_list, m):
        cnt = 0
        for word_set in word_set_list:
            if word_set < set(char_set) or word_set == set(char_set): cnt += 1
        max_cnt = max(max_cnt, cnt)
    return max_cnt
    
n, k = map(int, input().split())
word_list = [input() for _ in range(n)]

print(get_max_count2(k, word_list))

#흠... 맞왜틀.....