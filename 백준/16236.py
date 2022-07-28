#아기상어 - 수정 (min heap 활용)
from heapq import heappop, heappush

def solution(n, matrix):
    sx, sy = 0, 0
    fish_lst = [] #물고기 목록
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 9:
                sx, sy = i, j
            elif 1 <= matrix[i][j] <= 6:
                fish_lst.append(matrix[i][j])
    queue = []
    heappush(queue, (0, sx, sy))
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    visited = [[False] * n for _ in range(n)]
    visited[sx][sy] = True
    size = 2 #아기상어 크기
    cnt = 0 #먹은 물고기 수
    res = 0
    while queue and fish_lst:
        if min(fish_lst) > size: #물고기 리스트에 남아 있는 물고기 중 제일 작은 애가 먹을 수 없는 물고기일때
            break
        d, cx, cy = heappop(queue)
        if 0 < matrix[cx][cy] < size and matrix[cx][cy] != 9: #먹을 수 있는 물고기
            cnt += 1
            if cnt == size:
                size += 1
                cnt = 0
            res += d
            fish_lst.remove(matrix[cx][cy]) #물고기 목록에서 삭제 -> 여기서 valueError 가 발생하는데 왜지...
            matrix[sx][sy] = 0 #상어 이동
            sx, sy = cx, cy
            matrix[sx][sy] = 9
            queue.clear() #큐, 방문 표시 초기화
            heappush(queue, (0, sx, sy))
            visited = [[False] * n for _ in range(n)]
            visited[sx][sy] = True
            continue
        for dx, dy in dirs:
            if 0 <= cx + dx < n and 0 <= cy + dy < n and not visited[cx+dx][cy+dy] and matrix[cx+dx][cy+dy] <= size:
                heappush(queue, (d + 1, cx + dx, cy + dy))
                visited[cx+dx][cy+dy] = True
    return res

n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
print(solution(n, matrix))