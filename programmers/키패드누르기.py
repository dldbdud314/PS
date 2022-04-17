def getPos(key):
    return {1: (0, 0), 2: (0, 1), 3: (0, 2), 4: (1, 0), 5: (1, 1), 6: (1, 2), 7: (2, 0), 8: (2, 1), 9: (2, 2), 0: (3, 1)}.get(key)

#L/R 중 어느건지, 그 위치까지 return
def getMinLR(l, r, target):
    l_len = abs(target[0]-l[0]) + abs(target[1]-l[1])
    r_len = abs(target[0]-r[0]) + abs(target[1]-r[1])
    if l_len < r_len:
        return 'L', target
    elif l_len > r_len:
        return 'R', target
    else:
        return 'S', target

def solution(numbers, hand):
    l = {1, 4, 7}
    r = {3, 6, 9}
    lr = {2, 5, 8, 0}
    answer = ''
    cur_L, cur_R = (3, 0), (3, 2)
    for number in numbers:
        if number in l:
            cur_L = getPos(number)
            answer += 'L'
        elif number in r:
            cur_R = getPos(number)
            answer += 'R'
        else:
            h, pos = getMinLR(cur_L, cur_R, getPos(number))
            if h == 'L':
                cur_L = pos
                answer += 'L'
            elif h == 'R':
                cur_R = pos
                answer += 'R'
            else:
                if hand == 'left': 
                    cur_L = pos
                    answer += 'L'
                else: 
                    cur_R = pos
                    answer += 'R'
    return answer