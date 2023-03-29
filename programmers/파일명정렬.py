"""
** 구현 (문자열)
"""


def to(idx, org):
    for i in range(len(org)):
        if org[i].isdigit():
            head = org[:i].lower()
            tail = ''  # 숫자
            for j in range(i, len(org)):
                if org[j].isdigit(): tail += org[j]
                else: break
            tail = int(tail)

            return head, tail, idx  # 기준 정렬 순으로 변환하여 return


def solution(files):
    mapped = {}  # (변환된 파일, 기존 파일, 순서)
    for i, file in enumerate(files):
        k = tuple(to(i, file))
        mapped[k] = file

    res = []
    for k in sorted(mapped.keys()):
        res.append(mapped[k])

    return res

