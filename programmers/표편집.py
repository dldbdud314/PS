def solution(n, k, cmd):
    table = [True] * n
    del_stack = []
    ptr = k
    last_idx = n-1 #'True'인 마지막 인덱스  
    for c in cmd:
        print(table, ptr)
        if c[0] == 'C':
            table[ptr] = False
            del_stack.append(ptr)
            if ptr == last_idx:
                while not table[ptr]: ptr -= 1
                last_idx = ptr
            else:
                while not table[ptr] and ptr < last_idx: ptr += 1
        elif c[0] == 'Z':
            restored_idx = del_stack.pop()
            table[restored_idx] = True
            if restored_idx > last_idx: last_idx = restored_idx
        elif c[0] == 'U':
            move = int(c[2])
            survived = list({i for i in range(n)} - set(del_stack))
            move %= len(survived)
            cnt = 0
            while cnt < move:
                ptr -= 1
                if table[ptr]: cnt += 1
        else:
            move = int(c[2])
            survived = list({i for i in range(n)} - set(del_stack))
            move %= len(survived)
            cnt = 0
            while cnt < move:
                ptr += 1
                if table[ptr]: cnt += 1
    return ''.join(['O' if table[i] else 'X' for i in range(n)])

print(solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]))