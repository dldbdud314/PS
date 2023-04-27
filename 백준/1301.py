"""
1301. 비즈 공예
try ) backtracking -> 시간 초과
"""
n = int(input())
marbles = []
for _ in range(n):
    marbles.append(int(input()))

# dp[i][k] = i번째에 k 구슬이 꿰어져 있을 때 방법의 수
# dp = [[0] * n for _ in range(sum(marbles))] -> 아 이게 아닌가 봄..!?
cnt = 0


def dfs(lst, cur_m):
    if len(lst) == sum(marbles):
        global cnt
        cnt += 1
        return

    if not lst:
        # 모든 종류의 구슬에 대해 한번씩 꿰서 넘기기
        for i in range(len(cur_m)):
            cur_m[i] -= 1
            dfs([i], cur_m)
            cur_m[i] += 1
    else:
        if len(lst) == 1:
            # 이전 구슬과 비교해서 구슬 꿰서 넘기기
            for i in range(len(cur_m)):
                if lst[0] != i and cur_m[i] > 0:
                    cur_m[i] -= 1
                    dfs(lst + [i], cur_m)
                    cur_m[i] += 1
        else:
            m = len(lst)
            # 전전 원소, 전 원소와 비교해서 구슬 꿰서 넘기기
            for i in range(len(cur_m)):
                if lst[m - 2] != i and lst[m - 1] != i and cur_m[i] > 0:
                    cur_m[i] -= 1
                    dfs(lst + [i], cur_m)
                    cur_m[i] += 1


dfs([], marbles[:])  # 경우의 수 세기

print(cnt)

"""
** dp -> 7차원 dp ,, ?! ㄷㄷ
"""
