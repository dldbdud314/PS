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
    time = 1
    x, y = 0, 0
    for t, dir in moves:
        cur_time = int(t) - time
        for _ in range(int(cur_time)):
            print(snake)
            dx, dy = cur_dir
            #벽 확인
            if x + dx < 0 or x + dx >= n or y + dy < 0 or y + dy >= n:
                return time
            #자기 몸 확인
            if (x+dx, y+dy) in snake:
                return time
            #사과 확인
            if board[x+dx][y+dy] == 1:
                board[x+dx][y+dy] = 0
            else:
                snake.pop() #꼬리 위치 업데이트
            x += dx
            y += dy 
            snake.appendleft((x, y)) #머리 위치       
            time += 1
        print(dir, cur_dir)
        cur_dir = turn_dir(dir, cur_dir)
        print("turn:", cur_dir)
    return time

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

#to be debugged