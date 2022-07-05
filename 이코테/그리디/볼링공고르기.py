#my: 단순 조합
def solution(n, balls):
    cnt = 0
    for i in range(n):
        for j in range(i+1, n):
            if balls[i] != balls[j]:
                cnt += 1
    return cnt

#시간복잡도 측면에서 훨씬 good -> O(m*m)
#위에는 O(n*n) (n은 1000까지, m은 10까지)
def solution2(m, balls):
    balls.sort()
    ball_map = [0] * m
    for ball in balls:
        ball_map[ball-1] += 1
    cnt = 0
    for i in range(m):
        cnt += (ball_map[i] * sum(ball_map[i+1:]))
    return cnt

n, m = map(int, input().split())
balls = list(map(int, input().split()))
print(solution(n, balls))
print(solution2(m, balls))