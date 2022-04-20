#가르침
from collections import defaultdict

def get_max_count(n, k, word_list):
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

n, k = map(int, input().split())
word_list = [input() for _ in range(n)]

print(get_max_count(n, k, word_list))

#흠... 맞왜틀.....