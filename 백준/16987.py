"""
16987. 계란으로 계란치기

** 백트래킹, dfs 활용 .. 은 알겠는데 코드를 못 짜겠 .. 아오 헷갈 ..
"""
import sys
sys.setrecursionlimit(10 ** 5)

max_cnt = 0  # 가장 많이 깬 개수


def dfs(idx, cur_eggs):  # idx : 현재 계란
    global max_cnt
    # 종료 조건
    if idx == len(eggs):
        cnt = 0
        for x in cur_eggs:  # 깨진 계란 개수 세기
            if x < 0:
                cnt += 1
        max_cnt = max(cnt, max_cnt)
        return

    if cur_eggs[idx] <= 0:  # 현재 계란이 깨짐
        dfs(idx + 1, cur_eggs[:])
    else:
        for i in range(len(eggs)):
            if cur_eggs[i] > 0 and i != idx:
                a1 = cur_eggs[idx] - eggs[i][1]
                a2 = cur_eggs[i] - eggs[idx][1]
                cur_eggs[idx], cur_eggs[i] = a1, a2

                dfs(idx + 1, cur_eggs[:])
        else:
            dfs(idx + 1, cur_eggs[:])


n = int(input())
eggs = []
for _ in range(n):
    d, w = map(int, input().split())
    eggs.append((d, w))

eggs_stat = []  # 계란 내구성 모음
for d, _ in eggs:
    eggs_stat.append(d)

picked = [False] * len(eggs)
dfs(0, eggs_stat[:])

print(max_cnt)
