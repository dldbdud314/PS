import re
from itertools import combinations


def is_valid(ps):
    for i in range(1, len(ps)):
        if ps[i] == ps[i - 1]: return False
    return True


def alternate(s):
    aset = set(s)
    # edge case
    if len(aset) < 2:
        return 0

    max_len = 0
    for two_letters in combinations(aset, 2):
        restr = re.sub(r'[^' + two_letters[0] + two_letters[1] + r']', '', s)
        if is_valid(restr):
            max_len = max(max_len, len(restr))

    return max_len
