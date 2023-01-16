"""시뮬레이션(구현)"""
from string import ascii_uppercase


def find_pos(letter, MAP):
    for i in range(5):
        for j in range(5):
            if MAP[i][j] == letter:
                return i, j


message = input()
key = input()

# key -> 5*5표에 넣기
i, j, flag = 0, 0, False
MAP = [[None] * 5 for _ in range(5)]
existing = set()  # 등장한 알파벳 저장
for c in key:
    if c not in existing:
        MAP[i][j] = c
        existing.add(c)
        j += 1
        if j >= 5:
            i += 1
            j = 0
        if i >= 5:
            flag = True
            break  # MAP 다 채운 상황

while not flag:
    for c in ascii_uppercase:
        if c == 'J':
            continue
        if c not in existing:
            MAP[i][j] = c
            existing.add(c)
            j += 1
            if j >= 5:
                i += 1
                j = 0
            if i >= 5:
                flag = True

# message의 쌍을 나누기
idx = 0
pairs = []
while idx < len(message):
    pair = message[idx:idx + 2] if idx + 2 <= len(message) else message[idx]
    if len(pair) == 1:
        new_pair = pair + 'X'
        idx += 1
    else:
        if pair[0] == pair[1]:  # 쌍 파괴하기
            new_pair = pair[0] + 'X' if pair[0] != 'X' else pair[0] + 'Q'
            idx += 1
        else:
            new_pair = pair[:]
            idx += 2
    pairs.append(new_pair)

# 규칙에 따라 암호화 하기
encoded = ''
for pair in pairs:
    first_pos = find_pos(pair[0], MAP)
    sec_pos = find_pos(pair[1], MAP)
    if first_pos[0] == sec_pos[0]:  # row가 일치하는 경우
        encoded += MAP[first_pos[0]][(first_pos[1] + 1) % 5] + MAP[sec_pos[0]][(sec_pos[1] + 1) % 5]
    elif first_pos[1] == sec_pos[1]:  # col이 일치하는 경우
        encoded += MAP[(first_pos[0] + 1) % 5][first_pos[1]] + MAP[(sec_pos[0] + 1) % 5][sec_pos[1]]
    else:
        encoded += MAP[first_pos[0]][sec_pos[1]] + MAP[sec_pos[0]][first_pos[1]]

print(encoded)
