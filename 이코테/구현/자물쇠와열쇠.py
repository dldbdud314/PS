def init_a(m, n, lock):
    a = [[0] * (2 * m + n) for _ in range(2 * m + n)]
    for i in range(m, m + n):
        for j in range(m, m + n):
            a[i][j] = lock[i - m][j - m]
    return a

def turn(key):
    new_key = []
    for i in range(len(key[0])):
        new_key.append([row[i] for row in key[::-1]])
    return new_key

def is_open(a, m, n):
    #for i in range(len(a)):
    #    print(a[i])
    for i in range(m, m + n):
        for j in range(m, m + n):
            if a[i][j] == 0 or a[i][j] == 2: #홈이 안 채워진 경우 or 돌기와 돌기가 만나는 경우
                return False
    return True

def solution(key, lock):
    m, n = len(key), len(lock)
    a = init_a(m, n, lock) #공간 초기화, 중간에 자물쇠 박제
    #열쇠 4번 회전 -> 이동하면서 겹치는 부분 확인
    for _ in range(4):
        for ki in range(n - m + 1, n + m):
            for kj in range(n - m + 1, n + m):
                for i in range(m):
                    for j in range(m):
                        a[ki + i][kj + j] += key[i][j]
                if is_open(a, m, n): #자물쇠를 열 수 있다면
                    return True 
                a = init_a(m, n, lock) #공간 초기화
        #90도 회전
        key = turn(key)
    return False
print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))
# 89.0/100.0