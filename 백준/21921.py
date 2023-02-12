'''
21921. 블로그
슬라이딩 윈도우
'''
n, x = map(int, input().split())
arr = list(map(int, input().split()))

s, e = 0, x - 1  # 시작, 끝 인덱스
cur_sum = sum(arr[s: e + 1])
max_sum, max_cnt = cur_sum, 1  # 최대 방문자 수, 기간 수
while True:
    if e + 1 >= n:
        break

    cur_sum -= arr[s]
    s += 1
    e += 1
    cur_sum += arr[e]

    if max_sum < cur_sum:
        max_sum = cur_sum
        max_cnt = 1
    elif max_sum == cur_sum:
        max_cnt += 1

print(max_sum, max_cnt, sep='\n') if max_sum > 0 else print("SAD")
