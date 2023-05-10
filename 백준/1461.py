"""
1461. 도서관
- Greedy
양수/음수 리스트로 나누고, 절댓값 내림차순 정렬
각 리스트 m개 묶음으로 자르되, 가장 큰 값이 포함된 묶음은 한번만 더할 것 (*2 안함)
"""
n, m = map(int, input().split())
positions = list(map(int, input().split()))

# 양, 음 묶음 나누기 -> 절댓값 내림차순 정렬
negatives, positives = [], []
for position in positions:
    if position > 0:
        positives.append(position)
    else:
        negatives.append(position)

negatives.sort(key=lambda x: -abs(x))
positives.sort(key=lambda x: -x)

# 가장 큰 값
total = 0
b1 = negatives[0] if negatives and abs(negatives[0]) else 0
b2 = positives[0] if positives and positives[0] else 0
biggest = b1 if abs(b1) > b2 else b2

idx1 = 0  # 음수 리스트 처리
while idx1 < len(negatives):
    dist = negatives[idx1]
    total += abs(dist) if biggest in negatives[idx1: idx1 + m] else abs(dist) * 2
    idx1 += m

idx2 = 0  # 양수 리스트 처리
while idx2 < len(positives):
    dist = positives[idx2]
    total += dist if biggest in positives[idx2: idx2 + m] else dist * 2
    idx2 += m

print(total)

# 구현보단 아이디어 떠올리는 게 더 까다로움 !!
