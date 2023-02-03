"""
DP -> 위에 두 칸 중 더 큰 SUM 값 채택
dp[i+1][j] = max(dp[i][j] + x, dp[i][j+1] + x)

71.4 / 100.0 뭐여..!! -> 경계값 처리 오류 !

수정 : DP 배열 따로 안 만들고 주어진 triangle 갱신해가며 써먹기 ~
"""


def solution(triangle):
    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])):
            # 경계값 처리
            if j == 0:
                triangle[i][j] = triangle[i - 1][j] + triangle[i][j]
            elif j == len(triangle[i]) - 1:
                triangle[i][j] = triangle[i - 1][j - 1] + triangle[i][j]
            else:  # 사잇값 처리
                triangle[i][j] = max(triangle[i - 1][j - 1] + triangle[i][j], triangle[i - 1][j] + triangle[i][j])

    return max(triangle[-1])


print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))
