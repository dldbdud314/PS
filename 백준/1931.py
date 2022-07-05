def solution(rooms):
    rooms.sort(key=lambda x:(x[1], x[0]))
    ans = 0
    prev_e = 0
    for s, e in rooms:
        if prev_e <= s:
            ans += 1
            prev_e = e
    return ans

n = int(input())
rooms = []
for i in range(n):
    s, e = map(int, input().split())
    rooms.append([s, e])
print(solution(rooms))