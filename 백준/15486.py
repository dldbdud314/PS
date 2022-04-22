#퇴사2
def get_max_profit(n, works):
    dp = [[0]*(n+1) for _ in range(n)]
    #dp[i][j]: i를 시작으로 잡았을 때, 스탭 j에서의 profit 값
    dp_results = []
    
    for i in range(n):
        j = 0
        cur_day = i #시작일 설정
        while cur_day < len(works) and cur_day + works[cur_day][0] <= n:
            #print(cur_day)
            dp[i][j+1] = dp[i][j] + works[cur_day][1]
            cur_day += works[cur_day][0]
            j += 1
        #print(dp[i])
        dp_results.append(dp[i][j])
    #print(dp_results)
    return max(dp_results)

n = int(input())
works = []
for _ in range(n):
    a, b = map(int, input().split())
    works.append((a, b))
print(get_max_profit(n, works))