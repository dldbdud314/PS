#팰린드롬 만들기
'''
- Counter로 각 문자가 나온 횟수 기록
- 만약 홀수개가 나온 게 1보다 크면 팰린드롬 만들 수 없음
- 홀수개 나온 문자 가운데에 박제하고
- 나머지 문자 나온 횟수/2 만큼 리스트로 만들어서
- 순회하면서 앞, 뒤로 해당 문자 추가
'''
from collections import Counter

def solution(name):
    counter = Counter(name)
    odd_cnt = 0
    for v in counter.values():
        if v % 2 == 1: odd_cnt += 1 
    if odd_cnt > 1:
        return "I'm Sorry Hansoo"
    else:
        pelindrome = [''] * len(name)
        if odd_cnt == 1:
            odd_key = 0
            for k, v in counter.items():
                if v % 2 == 1: odd_key = k
            pelindrome[len(name)//2] = odd_key
            counter[odd_key] -= 1
        name_count = list(map(lambda x : (x[0], x[1] // 2), sorted(counter.items())))
        name_lst = ''
        for k, v in name_count:
            name_lst += (k * v)
        s, e = 0, len(name) - 1
        for x in name_lst:
            pelindrome[s] = x
            pelindrome[e] = x
            s += 1
            e -= 1
        return ''.join(pelindrome)

name = input()
print(solution(name))