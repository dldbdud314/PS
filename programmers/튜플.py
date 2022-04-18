def solution(s):
    s = s[2:-2]
    s_lst = s.split('},{')
    tuple_lst = []
    for ss in s_lst:
        tuple_lst.append(set(map(int, ss.split(','))))
    tuple_lst.sort()
    
    res = []
    last_tuple = set() #update용
    for tuple in tuple_lst:
        dif = tuple - last_tuple
        res.append(list(dif)[0])
        last_tuple.add(list(dif)[0])
        
    return res