

def valid_when_reversed(idxes, arr1, arr2):
    return tuple(arr1[idxes[-1]:idxes[0]:-1]) == tuple(arr2[idxes[0]:idxes[-1]])


def almostSorted(arr):
    sarr = sorted(arr)

    idx = 0
    idxes = []
    for x1, x2 in zip(arr, sarr):
        if x1 != x2:
            idxes.append(idx)
        idx += 1

    if not idxes:
        print("yes")
    elif len(idxes) == 2 and arr[idxes[0]] == sarr[idxes[1]] and arr[idxes[1]] == sarr[idxes[0]]:
        print("yes")
        print(f'swap {idxes[0] + 1} {idxes[1] + 1}')
    elif valid_when_reversed(idxes, arr, sarr):
        print("yes")
        print(f'reverse {idxes[0] + 1} {idxes[-1] + 1}')
    else:
        print("no")


almostSorted([1, 5, 4, 3, 2, 6])
