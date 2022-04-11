from itertools import combinations

def solution(orders, course):
    order_set_list = [set(order) for order in orders]
    menu_set = set()
    for order in orders:
        menu_set.update(list(order))
    ans = []
    for x in course:
        combinations_list = list(combinations(menu_set, x))
        combinations_set_list = list(map(set, combinations_list))
        
        largest_combination = []
        largest = -float('inf')
        for combination in combinations_set_list:
            cnt = 0
            for order in order_set_list:
                if combination < order or combination == order: cnt += 1
            if cnt > largest and cnt >= 2:
                largest = cnt
                largest_combination.clear()
                largest_combination.append(combination)
            elif cnt == largest:
                largest_combination.append(combination)
        ans.extend([''.join(sorted(list(x))) for x in largest_combination])
    return sorted(ans)

print(solution(["XYZ", "XWY", "WXA"], [2,3,4]))

#13, 14, 15 시간초과
