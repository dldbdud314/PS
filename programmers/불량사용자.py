from itertools import product

def match(banned, user_id):
    lst = []
    for u in user_id:
        if len(u) == len(banned):
            flag = True
            for x1, x2 in zip(banned, u):
                if x1 != '*' and x1 != x2:
                    flag = False
                    break
            if flag: lst.append(u)
    return lst

def solution(user_id, banned_id):
    banned_lst = []
    for b in banned_id:
        banned_lst.append(match(b, user_id))
    p = set()
    for x in product(*banned_lst):
        if len(set(x)) == len(x):
            p.add(tuple(sorted(x)))
    return len(p)

print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"]))
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"]))
