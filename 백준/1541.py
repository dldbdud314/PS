"""
1541. 잃어버린 괄호

** 문자열 파싱 + 그리디
- '-' 기준 파싱해서 연산 단위별 저장
    - 단위별 돌면서 연산
"""
s = input()

# 파싱
datas = s.split('-')

datas_summed = []  # 단위당 계산한 결과
for data in datas:
    datas_summed.append(sum(map(int, data.split('+'))))

# 연산
res = datas_summed[0]
for i in range(1, len(datas_summed)):
    res -= datas_summed[i]

print(res)
