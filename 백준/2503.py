#숫자야구
from itertools import permutations

N = int(input())
datas = []
for _ in range(N):
    num, s, b = map(int, input().split())
    datas.append([str(num), s, b])

cnt = 0
for x in permutations(list(range(1, 10)), 3):
    flag = True
    for num, strike, ball in datas:
        btmp, stmp = 0, 0
        for i in range(3):
            if int(num[i]) == x[i]:
                stmp += 1
            elif int(num[i]) in x:
                btmp += 1
        if stmp != strike or btmp != ball: #주어진 조건 하나라도 만족 못하면 
            flag = False
            break
    if flag: cnt += 1
    
print(cnt)