#우유 도시
def isDrinkable(last, cur):
    if last == 0 and cur == 1:
        return True
    elif last == 1 and cur == 2:
        return True
    elif last == 2 and cur == 0:
        return True
    return False

def solution(n, area):
    isValid = [[False] * (n+1) for _ in range(n+1)]
    dp = [[0] * (n+1) for _ in range(n+1)]
    dp[1][1] = 1
    isValid[1][1] = True
    for i in range(1, n+1):
        for j in range(1, n+1):
            if [i, j] == [1, 1]: continue
            if (isValid[i-1][j] and isDrinkable(area[i-1][j], area[i][j])) and (isValid[i][j-1] and isDrinkable(area[i][j-1], area[i][j])): #둘다
                dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + 1
                isValid[i][j] = True
            elif isValid[i-1][j] and isDrinkable(area[i-1][j], area[i][j]): #하나만
                dp[i][j] = dp[i-1][j] + 1
                isValid[i][j] = True
            elif isValid[i][j-1] and isDrinkable(area[i][j-1], area[i][j]):
                dp[i][j] = dp[i][j-1] + 1
                isValid[i][j] = True
            else: #둘다X -> validation
                if isValid[i-1][j] and isValid[i][j-1]:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                    isValid[i][j] = True
                elif isValid[i-1][j]:
                    dp[i][j] = dp[i-1][j]
                    isValid[i][j] = True
                elif isValid[i][j-1]:
                    dp[i][j] = dp[i][j-1]
                    isValid[i][j] = True
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1])
                    isValid[i][j] = False       
    print(isValid, dp)
    return dp[n][n]
#수정중.. isValid 검토하기

def solution1(n, area):
    dp = [[0] * (n+1) for _ in range(n+1)]
    dp[1][1] = 1
    for i in range(1, n+1):
        for j in range(1, n+1):
            if [i, j] == [1, 1]: continue
            if isDrinkable(area[i-1][j], area[i][j]) and isDrinkable(area[i][j-1], area[i][j]): #둘다
                dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + 1
            elif isDrinkable(area[i-1][j], area[i][j]): #하나만
                dp[i][j] = dp[i-1][j] + 1
            elif isDrinkable(area[i][j-1], area[i][j]):
                dp[i][j] = dp[i][j-1] + 1
            else: #둘다X
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[n][n]
# 반례: 0 -> 2 -> 0 도 계산한다! 여태까지 순서를 잘 따른 값이 dp에 담겨야..!!

n = int(input())
area = [[-1] * (n+1) for _ in range(n+1)]
for i in range(1, n+1):
    area[i][1:n+1] = map(int, input().split())
print(solution(n, area))