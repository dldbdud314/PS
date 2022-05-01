def initialize_linked_list(n):
    linked_list = [dict() for _ in range(n)]
    linked_list[0] = {'lp': -1, 'rp': 1} #-1은 end of list를 의미함
    for i in range(1, n-1):
        linked_list[i] = {'lp': i - 1, 'rp': i + 1}
    linked_list[n-1] = {'lp': n - 2, 'rp': -1}
    return linked_list

def solution(n, k, cmd):
    linked_list = initialize_linked_list(n)
    cp = k
    total_set = {i for i in range(n)}
    del_stack = []
    for x in cmd:
        if x[0] == 'U':
            move = int(x[2])
            cur_list = list(total_set - set(del_stack))
            cp = cur_list[cur_list.index(cp) - move]
        elif x[0] == 'D':
            move = int(x[2])
            cur_list = list(total_set - set(del_stack))
            cp = cur_list[cur_list.index(cp) + move]
        elif x[0] == 'C':
            del_stack.append(cp)
            left_idx = linked_list[cp]['lp']
            right_idx = linked_list[cp]['rp']
            if right_idx == -1: #cp == last node
                linked_list[left_idx]['rp'] = -1
                cp = left_idx
            else:    
                linked_list[left_idx]['rp'] = right_idx
                linked_list[right_idx]['lp'] = left_idx
                cp = right_idx       
        elif x[0] == 'Z':
            new_idx = del_stack.pop()
            left_idx = linked_list[new_idx]['lp']
            right_idx = linked_list[new_idx]['rp']
            linked_list[left_idx]['rp'] = new_idx
            linked_list[right_idx]['lp'] = new_idx
    return ''.join(['X' if i in set(del_stack) else 'O' for i in range(n)])
    
print(solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]))