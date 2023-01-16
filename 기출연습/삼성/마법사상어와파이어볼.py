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
            nexti = (curi + s * di) % N
            nextj = (curj + s * dj) % N
            after_move[(nexti, nextj)].append([m, s, d])
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