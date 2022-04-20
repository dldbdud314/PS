#빗물
h, w = map(int, input().split())
blocks = list(map(int, input().split()))

world = [[0]*w for _ in range(h)]
for j in range(w):
    for i in range(h-1, -1, -1):
        if h-1-i < blocks[j]:
            world[i][j] = 1

#가로줄 기준 count
#1을 표시하는 리스트를 둬서, 요소간 간격 = 빗물이 고이는 구간
total = 0
for i in range(h):
    cur_stack = []
    for j in range(w):
        if world[i][j] == 1: cur_stack.append(j)
    cur_total = 0
    for k in range(len(cur_stack)-1):
        cur_total += (cur_stack[k+1]-cur_stack[k]-1)
    total += cur_total
    
print(total)