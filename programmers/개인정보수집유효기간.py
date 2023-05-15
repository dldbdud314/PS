"""
** 문자열 처리, 구현
"""


def date_to_int(yy, mm, dd):
    return yy * 12 * 28 + mm * 28 + dd


def solution(today, terms, privacies):
    # today 파싱
    itoday = date_to_int(*map(int, today.split('.')))

    # terms 파싱
    tmap = dict()
    for term in terms:
        key, month = term.split()
        tmap[key] = date_to_int(0, int(month), 0)

    res = []
    # privacies 처리하기
    for idx, privacy in enumerate(privacies):
        pdate, t = privacy.split()
        pdate = date_to_int(*map(int, pdate.split('.')))

        if pdate + tmap[t] <= itoday:
            res.append(idx + 1)

    return res
