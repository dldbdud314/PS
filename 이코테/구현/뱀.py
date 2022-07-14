from collections import deque

def turn_dir(dir, cur_dir):
    if cur_dir == (0, 1): #right
        if dir == 'L': return (-1, 0)
        else: return (1, 0)
    elif cur_dir == (1, 0): #down
        if dir == 'L': return (0, 1)
        else: return (0, -1)
    elif cur_dir == (0, -1): #left
        if dir == 'L': return (1, 0)
        else: return (-1, 0)
    elif cur_dir == (-1, 0): #up
        if dir == 'L': return (0, -1)
        else: return (0, 1)

def solution(n, apples, moves):
    board = [[0]*n for _ in range(n)]
    for x, y in apples:
        board[x-1][y-1] = 1
    snake = deque([(0, 0)]) #뱀 위치
    cur_dir = (0, 1) #초기: 오른쪽으로
    time = 0
    x, y = 0, 0
    i = 0
    while True:
        if time == int(moves[i][0]): #방향 전환 시점이 되면
            cur_dir = turn_dir(moves[i][1], cur_dir)
            if i + 1 < len(moves): i += 1
        dx, dy = cur_dir
        #벽 확인
        if x + dx < 0 or x + dx >= n or y + dy < 0 or y + dy >= n: 
            break
        #자기 몸 확인
        if (x+dx, y+dy) in snake: 
            break
        #사과 확인
        if board[x+dx][y+dy] == 1:
            board[x+dx][y+dy] = 0
        else:
            snake.pop() #꼬리 위치 업데이트
        x += dx
        y += dy 
        snake.appendleft((x, y)) #머리 위치   
        time += 1
    return time + 1

n = int(input())
k = int(input())
apples = []
for _ in range(k):
    apples.append(tuple(map(int, input().split())))
l = int(input())
moves = []
for _ in range(l):
    moves.append(tuple(input().split()))
print(solution(n, apples, moves))