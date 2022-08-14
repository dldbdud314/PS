from collections import Counter
def solution(want, number, discount):
    cnt = 0
    want_dict = {k : v for k, v in zip(want, number)}
    for i in range(len(discount) - 9):
        if Counter(discount[i:i+10]) == want_dict:
            cnt += 1
    return cnt

print(solution(["apple"], [10], ["banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana"]))