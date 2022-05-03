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
    answer = ['O'] * n
    del_stack = []
    for x in cmd:
        if len(x) > 1:
            d, move = x.split()
            if d == 'U':
                for _ in range(int(move)): 
                    cp = linked_list[cp]['lp']
            elif d == 'D':
                for _ in range(int(move)): 
                    cp = linked_list[cp]['rp']
        else:
            if x == 'C':
                answer[cp] = 'X'
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
            else:
                new_idx = del_stack.pop()
                answer[new_idx] = 'O'
                left_idx = linked_list[new_idx]['lp']
                right_idx = linked_list[new_idx]['rp']
                linked_list[left_idx]['rp'] = new_idx
                linked_list[right_idx]['lp'] = new_idx
    return ''.join(answer)
    
print(solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]))

#ㅌㅔ스트케이스 하나 뭘까....ㅂㄷ