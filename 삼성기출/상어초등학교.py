#키 에러 웨얼

n = int(input())

seated = [[0] * n for _ in range(n)]

dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

my_likes = dict()

for _ in range(n * n):
    me, *likes = map(int, input().split())
    my_likes[me] = set(likes)
    
    check = [[0] * n for _ in range(n)] #자리별 좋아하는 사람의 인접 횟수 기록
    for like in likes:
        for i in range(n):
            for j in range(n):
                if seated[i][j] == like:
                    for di, dj in dirs:
                        if 0 <= i + di < n and 0 <= j + dj < n and seated[i+di][j+dj] == 0:
                            check[i+di][j+dj] += 1
    
    # 자주 등장한 건?
    most_frequent = 0 # 가장 큰 횟수
    for i in range(n):
        most_frequent = max(max(check[i]), most_frequent)
        
    # 해당 max count인 자리가 여러개인지
    most_frequent_count = 0
    freq_i, freq_j = 0, 0
    for i in range(n):
        for j in range(n):
            if check[i][j] == most_frequent:
                most_frequent_count += 1
                freq_i, freq_j = i, j
                
    if most_frequent_count == 1:
        seated[freq_i][freq_j] = me
    elif most_frequent_count > 1:
        seat_empty = dict()
        for i in range(n):
            for j in range(n):
                if check[i][j] == most_frequent:
                    seat_empty[(i, j)] = 0 #인접 빈칸 많은 애 찾기
                    for di, dj in dirs: #인접한 빈칸 개수 통계
                        if 0 <= i + di < n and 0 <= j + dj < n and seated[i+di][j+dj] == 0:
                            seat_empty[(i, j)] += 1 
        seat_sorted = sorted(seat_empty.items(), key = lambda x : (-x[1], x[0]))
        si, sj = seat_sorted[0][0] #(x, y)
        seated[si][sj] = me
        
total = 0       
for i in range(n):
    for j in range(n):
        cnt = 0
        me = seated[i][j]
        for di, dj in dirs:
            if 0 <= i + di < n and 0 <= j + dj < n:
                if seated[i+di][j+dj] in my_likes[me]:
                    cnt += 1
        if cnt > 0:
            total += 10 ** (cnt-1)

print(total)