#연구소3
from collections import deque
from itertools import combinations

def spread_virus_bfs(c, n, vlab):
    queue = deque(list(c))
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    while queue:
        x, y = queue.popleft()
        t = vlab[x][y]
        for dx, dy in dirs:
            #비활성 바이러스를 만나면 어떻게 처리? -> 시간은 count 하되, 최대 시간 계산할때 비활성 자리 count하면 안됨
            if 0 <= x + dx < n and 0 <= y + dy < n and (vlab[x+dx][y+dy] == -1 or vlab[x+dx][y+dy] == '*'):
                queue.append((x+dx, y+dy))
                vlab[x+dx][y+dy] = t + 1
                
def check_time(dc, n, vlab): #비활성 자리 빼고 count -> 비활성 자리가 최대치 갱신하기 때문
    biggest = -float('inf')
    for i in range(n):
        for j in range(n):
            if vlab[i][j] == '-' or (i, j) in dc:
                continue
            if vlab[i][j] == -1: return -1 #빈칸이 하나라도 있으면 fail
            else: biggest = max(biggest, vlab[i][j])
    return biggest

def lab_init(c, n, lab):
    vlab = [[-1] * n for _ in range(n)]
    dc = []
    for i in range(n):
        for j in range(n):
            if lab[i][j] == 0: #빈칸
                vlab[i][j] = -1
            elif lab[i][j] == 1: #벽
                vlab[i][j] = '-'
            elif lab[i][j] == 2:
                if (i, j) in c: vlab[i][j] = 0 #활성
                else: #비활성
                    vlab[i][j] = '*' 
                    dc.append((i, j))
    return vlab, dc

def solution(n, m, lab):
    viruses = []
    for i in range(n):
        for j in range(n):
            if lab[i][j] == 2: viruses.append((i, j))
    smallest = 999999
    for c in combinations(viruses, m):
        vlab, dc = lab_init(c, n, lab)
        spread_virus_bfs(c, n, vlab)
        t = check_time(dc, n, vlab)
        if t != -1:
            smallest = min(t, smallest)
    return -1 if smallest == 999999 else smallest

n, m = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(n)]
print(solution(n, m, lab))