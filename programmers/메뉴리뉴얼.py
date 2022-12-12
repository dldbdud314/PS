from itertools import combinations
from collections import Counter


def solution(orders, course):
    counts_per_course = [[] for _ in range(len(course))]
    for order in orders:
        for i, num in enumerate(course):
            for combi in combinations(sorted(list(order)), num):
                counts_per_course[i].append(''.join(combi))

    res = []
    for course_counts in counts_per_course:
        if not course_counts:
            break
        counts = Counter(course_counts)
        max_count = max(counts.values())
        for k, v in counts.items():
            if v >= 2 and v == max_count:
                res.append(k)

    return sorted(res)