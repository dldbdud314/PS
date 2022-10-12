n = int(input())

seated = [[0] * n for _ in range(n)]

dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

my_likes = dict()

for _ in range(n * n):
    me, *likes = map(int, input().split())
    my_likes[me] = set(likes)
    
    empty_seats = dict()
    
    for i in range(n):
        for j in range(n):
            if seated[i][j] == 0:
                like_cnt, empty_cnt = 0, 0
                for di, dj in dirs:
                    if 0 <= i + di < n and 0 <= j + dj < n:
                        if seated[i+di][j+dj] == 0:
                            empty_cnt += 1
                        elif seated[i+di][j+dj] in set(likes):
                            like_cnt += 1
                empty_seats[(i, j)] = [like_cnt, empty_cnt]
                
    seat_sorted = sorted(empty_seats.items(), key = lambda x : (-x[1][0], -x[1][1], x[0]))
    ii, jj = seat_sorted[0][0]
    seated[ii][jj] = me
    
total = 0
for i in range(n):
    for j in range(n):
        me = seated[i][j]
        cnt = 0
        for di, dj in dirs:
            if 0 <= i + di < n and 0 <= j + dj < n:
                if seated[i+di][j+dj] in my_likes[me]:
                    cnt += 1
        if cnt > 0:
            total += 10 ** (cnt - 1)

print(total)