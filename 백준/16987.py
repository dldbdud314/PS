"""
16987. 계란으로 계란치기

** 백트래킹, dfs 활용
"""
import sys
sys.setrecursionlimit(10 ** 5)

max_cnt = 0  # 가장 많이 깬 개수


def dfs(idx):  # idx : 현재 든 계란
    global max_cnt
    # 종료 조건
    if idx == len(eggs):
        cnt = 0
        for x, _ in eggs:  # 깨진 계란 개수 세기
            if x <= 0:
                cnt += 1
        max_cnt = max(cnt, max_cnt)
        return

    if eggs[idx][0] <= 0:  # 현재 계란이 깨짐
        dfs(idx + 1)  # 오른쪽 계란 들고 진행
    else:
        all_cracked = True
        for i in range(len(eggs)):
            if eggs[i][0] > 0 and i != idx:
                all_cracked = False
                eggs[idx][0] -= eggs[i][1]
                eggs[i][0] -= eggs[idx][1]
                dfs(idx + 1)
                eggs[idx][0] += eggs[i][1]
                eggs[i][0] += eggs[idx][1]
        if all_cracked:  # 더 꺨 수 없는 경우
            dfs(len(eggs))


n = int(input())
eggs = []
for _ in range(n):
    d, w = map(int, input().split())
    eggs.append([d, w])

dfs(0)

print(max_cnt)
