def solution(num):
    str_num = str(num)
    left_sum = 0
    for s in str_num[0:len(str_num)//2]:
        left_sum += int(s)
    right_sum = 0
    for s in str_num[len(str_num)//2:]:
        right_sum += int(s)
    return "LUCKY" if left_sum == right_sum else "READY"

num = int(input())
print(solution(num))