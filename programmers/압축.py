def solution(msg):
    dictionary = {chr(64+i) : i for i in range(1, 27)}
    last_idx = 26
    ans = []
    s = 0
    e = s + 1
    while e <= len(msg):
        if msg[s:e] not in dictionary:
            last_idx += 1
            dictionary[msg[s:e]] = last_idx
            ans.append(dictionary[msg[s:e-1]])
            s = e - 1
        else:
            if e == len(msg):
                ans.append(dictionary[msg[s:e]])
            e += 1
    return ans
print(solution("KAKAO"))
print(solution("TOBEORNOTTOBEORTOBEORNOT"))
print(solution("ABABABABABABABAB"))