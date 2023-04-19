"""
1) 기본적인 구현 방식
-> 찾기 함수가 비효율적으로 동작 가능 : O(V)

ex. union(4, 5) -> union(3, 4) -> union(2, 3) -> union(1, 2)
cur_node: 1 2 3 4 5
parent :  1 1 2 3 4

find(5): 5 -> 4 -> 3 -> 2 -> 1
"""


def find_parentX(p, x):
    # 자기 자신을 찾을 때까지 거슬러 올라가기
    if p[x] != x:
        return find_parentX(p, p[x])
    return x


"""
2) find_parent 최적화 -> 경로 압축
- parent 테이블 값이 root 노드로 기입

cur_node: 1 2 3 4 5
parent :  1 1 1 1 1
"""


def find_parent(p, x):
    # 루트 노드로 설정
    if p[x] != x:
        p[x] = find_parent(p, p[x])
    return p[x]


# 두 노드가 속한 집합 합치기 -> 노드 1, 2는 동일한 부모를 가지게 됨
def union_parent(p, n1, n2):
    p1 = find_parent(p, n1)
    p2 = find_parent(p, n2)
    if p1 < p2:  # 번호가 더 작은 쪽을 부모로 설정하기
        p[n2] = p1
    else:
        p[n1] = p2


v, e = map(int, input().split())
parent = [i for i in range(v + 1)]  # 자기자신을 부모로 초기화

# 주어진 간선 정보에 대해 union 연산 수행
for _ in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a, b)

# 각 원소가 속한 집합 출력
for i in range(1, v + 1):
    print(find_parent(parent, i), end=' ')

# 부모 테이블 출력
# print()
# for i in range(1, v + 1):
#     print(parent[i], end=' ')
