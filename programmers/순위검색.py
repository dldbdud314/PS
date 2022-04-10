def solution(info, query):
    info_arr = [a.split() for a in info]
    query_arr = [b.split() for b in query]
    
    res = []
    for query in query_arr:
        cur_res = 0
        for info in info_arr:
            lang, part, exp, food, score = info[0], info[1], info[2], info[3], info[4]
            if query[0] == '-': lang = '-'
            if query[2] == '-': part = '-'
            if query[4] == '-': exp = '-'
            if query[6] == '-': food = '-'
            if query[0] == lang and query[2] == part and query[4] == exp and query[6] == food and int(score) >= int(query[7]):
                cur_res += 1
        res.append(cur_res)
    return res
    
solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"], ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"])