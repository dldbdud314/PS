"""
13164. 행복 유치원

** 그리디 -> 풀이 참고 (구현 방식 떠올리기 어려웠음)
- 원생 간 차이값 계산
- 차이값 정렬 후, 상위 (k-1)개 탈락
- 나머지 합 구하기
"""
import sys

input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(map(int, input().split()))

# 차이값 갱신
diffs = []
for i in range(1, n):
    diffs.append(arr[i] - arr[i - 1])  # 차이값, 위치값

diffs.sort()  # 차이 오름차순 정렬
for _ in range(k-1):  # k개의 그룹으로 나누면 k-1번 짜른다
    diffs.pop()

print(sum(diffs))
