"""
10775. 공항
** Union Find (+그리디 아이디어)
"""
G = int(input())  # 게이트 수
P = int(input())  # 뱅기 수

parent = [i for i in range(G + 1)]

planes = []
for _ in range(P):
    planes.append(int(input()))


def find_parent(cur):
    if parent[cur] != cur:
        parent[cur] = find_parent(parent[cur])
    return parent[cur]


cnt = 0
for plane in planes:
    p = find_parent(plane)
    if p == 0:
        break
    parent[p] = parent[p - 1]  # union
    cnt += 1

print(cnt)
'''
** 단순 이중 반복문 -> 시간 초과(=10000 * 10000) -> ㅇㅇ 당연함

G = int(input())
P = int(input())

planes = []
for _ in range(P):
    planes.append(int(input()))

vis = [False] * G
for plane in planes:
    for i in range(plane - 1, -1, -1):
        if not vis[i]:
            vis[i] = True
            break
    else:
        break

print(vis.count(True))
'''

