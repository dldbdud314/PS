"""
연속 구간의 최대 합 구하기 -> ** DP 활용 (풀이 참고)

- dp[i] : i번째까지 최대 부분 합
- dp[i] = max(dp[i-1] + cur, cur) -> 기존 DP vs. 현재 부터 시작
"""


def solution(sequence):
    seq1 = [x * (-1) if i % 2 == 0 else x for i, x in enumerate(sequence)]
    seq2 = [x * (-1) if i % 2 == 1 else x for i, x in enumerate(sequence)]

    dp1, dp2 = [0] * len(sequence), [0] * len(sequence)
    dp1[0], dp2[0] = seq1[0], seq2[0]
    max_sum = max(dp1[0], dp2[0])
    for i in range(1, len(sequence)):
        dp1[i] = max(dp1[i - 1] + seq1[i], seq1[i])
        dp2[i] = max(dp2[i - 1] + seq2[i], seq2[i])

        max_sum = max(max_sum, dp1[i], dp2[i])

    return max_sum


print(solution([2, 3, -6, 1, 3, -1, 2, 4]))
