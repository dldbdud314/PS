# 내려가기 - 메모리 극극극 적게 써야함 !
n = int(input())
numbers = list(map(int, input().split()))  # 첫번쨰 줄
max_dp, min_dp = numbers, numbers
for _ in range(n - 1):  # 그 다음 줄 ~
    first, sec, third = map(int, input().split())

    new_max_dp, new_min_dp = [0] * 3, [0] * 3

    new_max_dp[0] = max(max_dp[0] + first, max_dp[1] + first)
    new_min_dp[0] = min(min_dp[0] + first, min_dp[1] + first)

    new_max_dp[1] = max(max_dp[0] + sec, max_dp[1] + sec, max_dp[2] + sec)
    new_min_dp[1] = min(min_dp[0] + sec, min_dp[1] + sec, min_dp[2] + sec)

    new_max_dp[2] = max(max_dp[1] + third, max_dp[2] + third)
    new_min_dp[2] = min(min_dp[1] + third, min_dp[2] + third)

    max_dp, min_dp = new_max_dp, new_min_dp


print(max(max_dp), min(min_dp))
