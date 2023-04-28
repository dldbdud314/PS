"""
** Greedy, 완탐

- 빠른 시작 시각 기준으로 정렬한 전체 데이터를
- 끝나는 시각들을 담은 rooms에 넣으면서 방별 끝나는 시각을 갱신한다
"""


def solution(book_time):
    book_secs = []  # 초 변환 후 저장
    for s, e in book_time:
        s_min, s_sec = map(int, s.split(':'))
        e_min, e_sec = map(int, e.split(':'))
        book_secs.append((s_min * 60 + s_sec, e_min * 60 + e_sec))
    book_secs.sort()  # 시작 시각 기준 정렬

    rooms = []  # 방별 가장 마지막 종료 시각
    for s, e in book_secs:
        if not rooms:
            rooms.append(e + 10)
            continue

        for i in range(len(rooms)):
            if rooms[i] <= s:
                rooms[i] = e + 10
                break
        else:
            rooms.append(e + 10)

    return len(rooms)
