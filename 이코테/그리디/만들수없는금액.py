from itertools import combinations
#my: 조합 활용 - 시간복잡도 걱정..ㅎ
def solution(coins):
    coins_set = set()
    for i in range(1, len(coins)+1):
        coins_set.update(set(map(sum, combinations(coins, i))))
    num = 1
    while True:
        if num in coins_set:
            num += 1
        else:
            break
    return num

n = int(input())
coins = list(map(int, input().split()))
print(solution(coins))