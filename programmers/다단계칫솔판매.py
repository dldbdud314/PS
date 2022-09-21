def solution(enroll, referral, seller, amount):
    graph = {e:r for e, r in zip(enroll, referral)}
    profit = {e : 0 for e in enroll}
    profit["-"] = 0
    for i in range(len(seller)):
        leaf = seller[i]
        money = amount[i] * 100  
        
        child = leaf
        cm, pm = money, 0
        while True:
            if child == '-':
                break
            parent = graph[child]
            tmp = cm // 10
            pm += tmp
            cm -= tmp
            profit[child] += cm
            if tmp == 0: break
            child = parent
            cm = pm
            pm = 0
    ans = []
    for x in enroll:
        ans.append(profit[x])
    return ans

print(solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"], ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"], ["sam", "emily", "jaimie", "edward"], [2, 3, 5, 4]))