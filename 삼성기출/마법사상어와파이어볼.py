from collections import defaultdict
from math import floor

N, M, K = map(int, input().split())

fireballs = defaultdict(list)

for _ in range(M):
    r, c, m, s, d = map(int, input().split())
    fireballs[(r-1, c-1)].append([m, s, d])
    
move = {0 : (-1, 0), 1 : (-1, 1), 2 : (0, 1), 3 : (1, 1), 4 : (1, 0), 5 : (1, -1), 6 : (0, -1), 7 : (-1, -1)}

for _ in range(K):
    after_move = defaultdict(list)
    #이동
    for pos, infos in fireballs.items():
        curi, curj = pos #해당 위치의
        for m, s, d in infos: #각각의 fireball 정보에 대해
            di, dj = move.get(d)
            nexti, nextj = curi, curj
            for _ in range(s): #s만큼 움직였을 때, 범위 밖으로 나가는 걸 고려
                nexti += di
                nextj += dj
                if nexti < 0: nexti = N - 1
                elif nexti >= N: nexti = 0
                if nextj < 0: nextj = N - 1
                elif nextj >= N: nextj = 0
            moved = [m, s, d]
            after_move[(nexti, nextj)].append(moved)
    fireballs = after_move
    #연산
    after_calc = defaultdict(list)
    for pos, infos in fireballs.items():
        if len(infos) > 1:
            msum, ssum = 0, 0 #질량합, 속력합
            checkd1, checkd2 = 0, 0 #짝홀 체크용
            for m, s, d in infos:
                msum += m
                ssum += s
                if d % 2 == 0: checkd1 += 1
                else: checkd2 += 1
            newm = floor(msum / 5)
            news = floor(ssum / len(infos))
            if checkd1 == len(infos) or checkd2 == len(infos):
                newds = [0, 2, 4, 6]
            else:
                newds = [1, 3, 5, 7]
            if newm > 0:    
                new_fireballs = []
                for i in range(4):
                    new_fireballs.append([newm, news, newds[i]])
                after_calc[pos].extend(new_fireballs)
        elif len(infos) == 1:
            after_calc[pos].append(infos[0])
    fireballs = after_calc

total = 0
for pos, infos in fireballs.items():
    for m, _, _ in infos:
        total += m
        
print(total)

# 처음에 자료구조 잘못 잡고 헤멤
# 시간 초과
# 덜 에바적인 풀이 함 볼까..?ㅋ