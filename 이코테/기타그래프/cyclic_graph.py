"""
** 사이클 여부 판별 알고리즘

간선 정보 1, 2에 대해 :
- 부모1 == 부모2 -> 같은 집합에 속함, 즉 사이클 존재
- 부모1 != 부모2 -> 합치기
"""


def find_parent(p, x):
    if p[x] != x:
        p[x] = find_parent(p, p[x])
    return p[x]


# 합치기 (두 노드는 서로 다른 집합인 게 보장)
def union_parent(p, x1, x2):
    if x1 < x2:  # 번호가 더 작은 쪽을 부모로 설정하기
        p[x2] = x1
    else:
        p[x1] = x2


v, e = map(int, input().split())
parent = [i for i in range(v + 1)]  # 자기자신을 부모로 초기화

# 주어진 간선 정보에 대해 연결 지으면서 사이클 여부 판별
is_cycle = False
for _ in range(e):
    a, b = map(int, input().split())

    p1 = find_parent(parent, a)
    p2 = find_parent(parent, b)
    if p1 == p2:  # 같은 집합에 속함
        is_cycle = True
        break
    else:  # 사이클 발생하지 않으면 Union 수행
        union_parent(parent, p1, p2)

print("사이클 발생") if is_cycle else print("사이클 없음")
