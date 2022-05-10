#그리디

#방법1. 전체 유니폼 목록 기록 -> O(n)
def solution1(n, lost, reserve):
    uniform = [1] * (n + 2)
    for r in reserve:
        uniform[r] += 1
    for l in lost:
        uniform[l] -= 1
    #이러면 아예 체육복이 없는 학생은 0, 체육복이 여벌로 있는 학생은 2인 uniform 배열이 된다.
    for i in range(1, n + 1):
        if uniform[i-1] == 0 and uniform[i] == 2:
            uniform[i-1], uniform[i] = 1, 1
        elif uniform[i] == 2 and uniform[i+1] == 0:
            uniform[i], uniform[i+1] = 1, 1
    return len([u for u in uniform[1:-1] if u > 0])

#방법2. set의 활용으로 포함 여부를 확인하는 방식 -> O(k log k)
def solution2(n, lost, reserve):
    s = set(lost) & set(reserve) #교집합
    l = set(lost) - s
    r = set(reserve) - s
    for x in sorted(r):
        if x - 1 in l:
            l.remove(x - 1)
        elif x + 1 in l:
            l.remove(x + 1)
    return n - len(l)