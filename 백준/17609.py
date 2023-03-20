"""
17609. 회문
** 투포인터 -> 풀이 참고 !
"""


def solution():
    S = input()

    # 완전한 회문인가?
    if S == S[::-1]:
        return 0

    # 1인가 2인가 -> 투포인터
    s, e = 0, len(S) - 1
    while s < e:
        # 불일치 하는 자리 찾을 때까지 좁혀 가기
        if S[s] == S[e]:
            s += 1
            e -= 1
        else:
            # 양쪽 끝 삭제 츄라이 ~ !
            ltmp, rtmp = S[s + 1: e + 1], S[s: e]
            if ltmp == ltmp[::-1] or rtmp == rtmp[::-1]:
                return 1
            else:
                return 2


t = int(input())
for _ in range(t):
    print(solution())
