"""구현"""
import sys
input = sys.stdin.readline


def rank_scores(rnd_scores):
    rndRanks = [0] * n

    rank = 1  # 공동 순위 처리용
    rndRanks[rnd_scores[0][1]] = rank
    for i in range(1, len(rnd_scores)):
        if rnd_scores[i - 1][0] > rnd_scores[i][0]:
            rank = i + 1
        rndRanks[rnd_scores[i][1]] = rank

    return rndRanks


n = int(input())
ranks = [[0] * n for _ in range(4)]  # 최종 등수 결과

total_scores = [0] * n  # 참가자별 최종 점수
for rnd in range(3):
    scores = []
    for i, score in enumerate(list(map(int, input().split()))):
        total_scores[i] += score
        scores.append((score, i))
    scores.sort(key=lambda x: -x[0])  # 점수 기준 내림차순 정렬

    ranks[rnd] = rank_scores(scores)

# 최종 등수 계산
scores = []
for i, score in enumerate(total_scores):
    scores.append((score, i))
scores.sort(key=lambda x: -x[0])
ranks[3] = rank_scores(scores)

for rank in ranks:
    print(*rank, sep=' ')
