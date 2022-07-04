#풀이방식: 연속되는 0의 개수, 1의 개수 구해서 그 중 더 작은 애
def solution(s):
    one_cnt, zero_cnt = 0, 0
    for i in range(1, len(s)):
        if s[i] == '1':
            if s[i-1] == '0':
                zero_cnt += 1
            if i == len(s)-1:
                one_cnt += 1
        else:
            if s[i-1] == '1':
                one_cnt += 1
            if i == len(s)-1:
                zero_cnt += 1
    return min(one_cnt, zero_cnt)

s = input()
print(solution(s))