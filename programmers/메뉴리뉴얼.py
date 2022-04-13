from itertools import combinations

def solution(orders, course):
    order_set_list = [set(order) for order in orders]
    menu_set = set()
    for order in orders:
        menu_set.update(list(order))
    ans = []
    for x in course:
        combinations_list = list(map(lambda m : list(combinations(m, x)), order_set_list))
        combinations_set = set()
        for combination in combinations_list:
            for e in combination:
                combinations_set.add(e)
        combinations_set_list = list(map(set, combinations_set))
        
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
    return sorted(list(set(ans)))