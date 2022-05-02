#점프
from collections import deque

#실패한 풀이
def get_paths_bfs(n, board):
    dp = [[0] * n for _ in range(n)]
    queue = deque([(0, 0)]) #시작점 (0, 0)
    while queue:
        cur_x, cur_y = queue.popleft()
        move = board[cur_x][cur_y]
        if cur_y + move < n and move > 0:
            dp[cur_x][cur_y+move] += 1
            queue.append((cur_x, cur_y + move))
        if cur_x + move < n and move > 0:
            dp[cur_x+move][cur_y] += 1
            queue.append((cur_x + move, cur_y))  
    return dp[n-1][n-1]
#메모리초과 - 아 큐를 쓰지 않는 게 답인가... 
#그렇다고 방문표시를 하면 답이 안 맞..
#bfs 사용 X -> 가장 먼저 도착지(n-1, n-1)에 도착하는 애가 있어서 제대로 반영안되는듯..

def get_paths_dp(n, board):
    dp = [[0] * n for _ in range(n)]
    dp[0][0] = 1
    for i in range(n):
        for j in range(n):
            jump = board[i][j]
            if jump == 0: break
            if jump + i < n:
                dp[jump+i][j] += dp[i][j]
            if jump + j < n:
                dp[i][jump+j] += dp[i][j]
    return dp[n-1][n-1]
#그래프 순회하면서 위치별 dp update하기

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
print(get_paths_dp(n, board))